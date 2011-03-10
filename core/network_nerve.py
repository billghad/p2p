#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Asyncore/asychat "mutated" to a network-nerve.
The central idea: represent the network as an 'organ' pool.
Organs may send/receive signals.
Simply connect the nervous system to this pool and communicate.

How it works:
1.wraps asyncore Server/Channels to coroutines (neuron, synapses) 
2.creates one filter-coroutine for simple (incoming)signal filtering
3.creates a signal transmitter for sending signals
4.transmits distinct signals over distinct synapses to a filter neuron.

Filters signals and/or transmits them to the output.
Provides some organ_id/synapse_id for further communication.

                           +-------+
+-----+            ------->|synapse|-------
|Input|           /        +-------+       \
+-----+\ +----- +/         +-------+        \  +------+      +------+
        \|neuron|--------->|synapse|---------->|filter|----->|output|
+-----+ /+----- +\         +-------+        /  +------+      +------+
|Input|/           \       +-------+       /
+-----+            ------->|synapse|-------
                           +-------+
                  
Creating:
n = NetworkNeuron()
n.associate(output)

The 'output' is a coroutine or an object implementing 'send' method
and consumes incoming signals.

Signal format: (organ_id/synapse, signal)

Attention:
Neurons need energy to transport their neurotransmitters!
Provide some energy(=time) or the neuron will not work correctly!

NetworkNeuron.feed(amount=(0,R+])
or
NetworkNeuron.feed()
"""

import asynchat
import asyncore
import socket

from decorators import coroutine
from config import network, logs
from signal_protocol import Signal, ProtocolError

@coroutine
def signal_transmitter():
    """ Collect outgoing signals, sends them back """
    try:
        while True:
            synapse, signal = (yield)            
            if synapse.is_active():
                try:
                    synapse.push(signal.serialize())
                    logs.logger.debug("signal_transmitter: %s, %s" %
                                      (synapse, signal))
                except ProtocolError, reason:
                    logs.logger.debug("signal_transmitter error: %s, %s" %
                                      (synapse, reason))                
    finally:
        logs.logger.debug("signal_transmitter closed")
        
@coroutine
def signal_filter(target, transmitter):
    """ Collects and validates input messages from synapses """
    try:
        while True:       
            synapse, data = (yield)
            try:
                logs.logger.debug("filters data from %s" % synapse)
                signal = Signal.deserialize(data)                
            except ProtocolError, reason:
                # low-level protocol error (e.g transmission of '[1,2' )
                logs.logger.debug("filter error: %s,%s" % (synapse, reason))
                err_response = Signal('error',
                                      (Signal.ProtocolError, str(reason)))
                transmitter.send((synapse, err_response))
                synapse.disconnect()
            else:                
                target.send((synapse, signal))
    finally:
        logs.logger.debug("signal filter closed")


class _Synapse(asynchat.async_chat):
    """ Asynchronous network channel mutated to a synapse."""

    def __init__(self, sock, organ_id, target):
        asynchat.async_chat.__init__(self, sock)
        if sock is None:
            print "connect"
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect(organ_id)
        self.organ_id = organ_id     
        self.set_terminator(Signal.TERMINATOR)
        self.buffer = []
        self.target = target
        self.collect_incoming_data = self.buffer.append

    def found_terminator(self):
        """ Sends received message to target and clears input buffer"""
        logs.logger.debug("%s sends data to %s" % (self, self.target.__name__))
        self.target.send((self, "".join(self.buffer)))
        del(self.buffer[:])        
        
    def is_active(self):
        """ provides information about synapse activity """
        return (self.accepting  == True) or (self.connected == True)

    def disconnect(self):
        """ flushes data and closes """
        self.close_when_done()
        logs.logger.debug("disconnect %s" % self)

    def __str__(self):
        """ A nice string representation for logging module """
        return "Synapse(%s <-> %s)" % (self.organ_id, self.target.__name__)
    
    def log(self, message):
        """ Overrides 'log' from asyncore module to produce consistent logs """
        logs.logger.debug("asyncore log: %s" % message)

    def log_info(self, message, msg_type='info'):
        """ Overrides 'log_info' from asyncore module (-> consistent logs) """
        logs.logger.debug("asyncore log: %s, %s" % (msg_type, message))  

        
class NeuronError(Exception):
    """ Serious/fatal error while creating a neuronal connection """
    pass


class NetworkNeuron(asyncore.dispatcher):
    """ Provides asynchronous network communication, represented by a
    neuronal connection.
    Expects: some output consumer (coroutine or an object implementing 'send' )
    Output format: (organ_id/synapse, message)"""
    def __init__(self, port=network.server_port):       
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        port_range = network.server_port_range + port
        # try to create a listener in predefined portrange:
        while port < port_range:        
            try:
                self.bind(('', port))
                self.listen(5)
            except socket.error, reason:
                logs.logger.warning("Error: could not bind socket." +
                                    "Port: %s already in use" % port)
                port += 1
            else:
                self.port = port
                break
        else:
            logs.logger.critical("Error: could not bind socket")
            raise NeuronError(reason)
        
        logs.logger.debug("listen to: %s" % port)
        self.signal_transmitter = signal_transmitter()

    def associate(self, target):
        """ connect with an putput processor """
        self.signal_filter = signal_filter(target, self.signal_transmitter)
        
    def log(self, message):
        """ Overrides 'log' from asyncore module to produce consistent logs """
        logs.logger.debug("asyncore log: %s" % message)

    def log_info(self, message, msg_type='info'):
        """ Overrides 'log_info from asyncore module (->consistent logs) """
        logs.logger.debug("asyncore log: %s, %s" % (msg_type, message))

    def connect(self, organ_id, target):
        return _Synapse(None, organ_id, target)
        
    def handle_accept(self):
        sock, organ_id = self.accept()
        logs.logger.debug("accepts: %s" % [organ_id])
        logs.logger.debug("connections: %s" % len(self._map))
        _Synapse(sock, organ_id, self.signal_filter)

    def feed(self, amount = network.default_listen_time):
        """ Feeds the neuron with some time. Neuron spends this time for
        network transmissions."""
        asyncore.loop(timeout = amount, count = 10)
        
