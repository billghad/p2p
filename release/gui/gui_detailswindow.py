#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from time import localtime, strftime


class Ui_DetailsWindow(object):
    def setupUi(self, DetailsWindow):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(404, 402)
        self.tabs = QtGui.QTabWidget(DetailsWindow)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 381, 381))
        self.tabs.setObjectName("tabs")
        self.tabDetails = QtGui.QWidget()
        self.tabDetails.setObjectName("tabDetails")
        self.cbSo = QtGui.QCheckBox(self.tabDetails)
        self.cbSo.setEnabled(False)
        self.cbSo.setGeometry(QtCore.QRect(318, 170, 45, 22))
        self.cbSo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbSo.setObjectName("cbSo")
        self.cbMo = QtGui.QCheckBox(self.tabDetails)
        self.cbMo.setEnabled(False)
        self.cbMo.setGeometry(QtCore.QRect(14, 170, 49, 22))
        self.cbMo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbMo.setObjectName("cbMo")
        self.leOrt = QtGui.QLineEdit(self.tabDetails)
        self.leOrt.setGeometry(QtCore.QRect(70, 40, 294, 27))
        self.leOrt.setReadOnly(True)
        self.leOrt.setObjectName("leOrt")
        self.cbMi = QtGui.QCheckBox(self.tabDetails)
        self.cbMi.setEnabled(False)
        self.cbMi.setGeometry(QtCore.QRect(117, 170, 44, 22))
        self.cbMi.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbMi.setObjectName("cbMi")
        self.teEnde = QtGui.QTimeEdit(self.tabDetails)
        self.teEnde.setGeometry(QtCore.QRect(70, 106, 294, 27))
        self.teEnde.setReadOnly(True)
        self.teEnde.setTime(QtCore.QTime(12, 0, 0))
        self.teEnde.setObjectName("teEnde")
        self.lbBeschreibung = QtGui.QLabel(self.tabDetails)
        self.lbBeschreibung.setGeometry(QtCore.QRect(10, 220, 351, 17))
        self.lbBeschreibung.setObjectName("lbBeschreibung")
        self.cbDi = QtGui.QCheckBox(self.tabDetails)
        self.cbDi.setEnabled(False)
        self.cbDi.setGeometry(QtCore.QRect(69, 170, 42, 22))
        self.cbDi.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbDi.setObjectName("cbDi")
        self.pteBeschreibung = QtGui.QPlainTextEdit(self.tabDetails)
        self.pteBeschreibung.setGeometry(QtCore.QRect(10, 243, 351, 91))
        self.pteBeschreibung.setReadOnly(True)
        self.pteBeschreibung.setObjectName("pteBeschreibung")
        self.lbTitel = QtGui.QLabel(self.tabDetails)
        self.lbTitel.setGeometry(QtCore.QRect(15, 7, 49, 27))
        self.lbTitel.setObjectName("lbTitel")
        self.cbDo = QtGui.QCheckBox(self.tabDetails)
        self.cbDo.setEnabled(False)
        self.cbDo.setGeometry(QtCore.QRect(167, 170, 47, 22))
        self.cbDo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbDo.setObjectName("cbDo")
        self.teBeginn = QtGui.QTimeEdit(self.tabDetails)
        self.teBeginn.setGeometry(QtCore.QRect(70, 73, 294, 27))
        self.teBeginn.setReadOnly(True)
        self.teBeginn.setTime(QtCore.QTime(11, 0, 0))
        self.teBeginn.setObjectName("teBeginn")
        self.lbEnde = QtGui.QLabel(self.tabDetails)
        self.lbEnde.setGeometry(QtCore.QRect(15, 106, 49, 27))
        self.lbEnde.setObjectName("lbEnde")
        self.lbBeginn = QtGui.QLabel(self.tabDetails)
        self.lbBeginn.setGeometry(QtCore.QRect(15, 73, 49, 27))
        self.lbBeginn.setObjectName("lbBeginn")
        self.lbOrt = QtGui.QLabel(self.tabDetails)
        self.lbOrt.setGeometry(QtCore.QRect(15, 40, 49, 27))
        self.lbOrt.setObjectName("lbOrt")
        self.leTitel = QtGui.QLineEdit(self.tabDetails)
        self.leTitel.setGeometry(QtCore.QRect(70, 7, 294, 27))
        self.leTitel.setReadOnly(True)
        self.leTitel.setObjectName("leTitel")
        self.cbFr = QtGui.QCheckBox(self.tabDetails)
        self.cbFr.setEnabled(False)
        self.cbFr.setGeometry(QtCore.QRect(220, 170, 42, 22))
        self.cbFr.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbFr.setChecked(False)
        self.cbFr.setObjectName("cbFr")
        self.cbSa = QtGui.QCheckBox(self.tabDetails)
        self.cbSa.setEnabled(False)
        self.cbSa.setGeometry(QtCore.QRect(268, 170, 44, 22))
        self.cbSa.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbSa.setObjectName("cbSa")
        self.lbKalendertage = QtGui.QLabel(self.tabDetails)
        self.lbKalendertage.setGeometry(QtCore.QRect(10, 150, 351, 17))
        self.lbKalendertage.setObjectName("lbKalendertage")
        self.tabs.addTab(self.tabDetails, "")
        self.tabChat = QtGui.QWidget()
        self.tabChat.setObjectName("tabChat")
        self.pteChat = QtGui.QPlainTextEdit(self.tabChat)
        self.pteChat.setGeometry(QtCore.QRect(10, 10, 351, 291))
        self.pteChat.setUndoRedoEnabled(False)
        self.pteChat.setReadOnly(True)
        self.pteChat.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.pteChat.setObjectName("pteChat")
        self.leNachricht = QtGui.QLineEdit(self.tabChat)
        self.leNachricht.setGeometry(QtCore.QRect(10, 310, 281, 27))
        self.leNachricht.setObjectName("leNachricht")
        self.pbSenden = QtGui.QPushButton(self.tabChat)
        self.pbSenden.setGeometry(QtCore.QRect(300, 310, 61, 27))
        self.pbSenden.setObjectName("pbSenden")
        self.tabs.addTab(self.tabChat, "")

        self.retranslateUi(DetailsWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DetailsWindow)
        DetailsWindow.setTabOrder(self.tabs, self.leTitel)
        DetailsWindow.setTabOrder(self.leTitel, self.leOrt)
        DetailsWindow.setTabOrder(self.leOrt, self.teBeginn)
        DetailsWindow.setTabOrder(self.teBeginn, self.teEnde)
        DetailsWindow.setTabOrder(self.teEnde, self.cbMo)
        DetailsWindow.setTabOrder(self.cbMo, self.cbDi)
        DetailsWindow.setTabOrder(self.cbDi, self.cbMi)
        DetailsWindow.setTabOrder(self.cbMi, self.cbDo)
        DetailsWindow.setTabOrder(self.cbDo, self.cbFr)
        DetailsWindow.setTabOrder(self.cbFr, self.cbSa)
        DetailsWindow.setTabOrder(self.cbSa, self.cbSo)
        DetailsWindow.setTabOrder(self.cbSo, self.pteBeschreibung)
        DetailsWindow.setTabOrder(self.pteBeschreibung, self.pteChat)
        DetailsWindow.setTabOrder(self.pteChat, self.leNachricht)
        DetailsWindow.setTabOrder(self.leNachricht, self.pbSenden)

    def retranslateUi(self, DetailsWindow):
        DetailsWindow.setWindowTitle(QtGui.QApplication.translate("DetailsWindow", "Detailansicht", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSo.setText(QtGui.QApplication.translate("DetailsWindow", "So", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMo.setText(QtGui.QApplication.translate("DetailsWindow", "Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMi.setText(QtGui.QApplication.translate("DetailsWindow", "Mi", None, QtGui.QApplication.UnicodeUTF8))
        self.lbBeschreibung.setText(QtGui.QApplication.translate("DetailsWindow", "Beschreibung:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDi.setText(QtGui.QApplication.translate("DetailsWindow", "Di", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTitel.setText(QtGui.QApplication.translate("DetailsWindow", "Titel:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDo.setText(QtGui.QApplication.translate("DetailsWindow", "Do", None, QtGui.QApplication.UnicodeUTF8))
        self.lbEnde.setText(QtGui.QApplication.translate("DetailsWindow", "Ende:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbBeginn.setText(QtGui.QApplication.translate("DetailsWindow", "Beginn:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbOrt.setText(QtGui.QApplication.translate("DetailsWindow", "Ort:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFr.setText(QtGui.QApplication.translate("DetailsWindow", "Fr", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSa.setText(QtGui.QApplication.translate("DetailsWindow", "Sa", None, QtGui.QApplication.UnicodeUTF8))
        self.lbKalendertage.setText(QtGui.QApplication.translate("DetailsWindow", "Kalendertage:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabDetails), QtGui.QApplication.translate("DetailsWindow", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSenden.setText(QtGui.QApplication.translate("DetailsWindow", "&Senden", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabChat), QtGui.QApplication.translate("DetailsWindow", "Chat", None, QtGui.QApplication.UnicodeUTF8))







class MyDetailsWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDetailsWindow, self).__init__(parent)
        self.ui = Ui_DetailsWindow()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.pbSenden, QtCore.SIGNAL('clicked()'), self.pbSendenClicked)
        QtCore.QObject.connect(self.ui.tabs, QtCore.SIGNAL("currentChanged(int)"), self.tabCurrentChanged)

    def tabCurrentChanged(self, id):
        if id == 1:
            self.ui.leNachricht.setFocus()
            
    def insertChatMessage(self, inChatMessage, inNick):
        self.ui.pteChat.insertPlainText("[" + strftime("%H:%M:%S", localtime()) + "] "+ inNick +": " + inChatMessage + "\n")
        ''' AutoScroll '''
        self.ui.pteChat.verticalScrollBar().setValue(self.ui.pteChat.verticalScrollBar().maximum())
        
    def pbSendenClicked(self):
        self.chatMessage = self.ui.leNachricht.text()
        if len(self.chatMessage) <= 0:
            self.ui.leNachricht.setFocus()
            return
        
        self.parent().brain.sendChatMsg(self.chatMessage, self.myUuid)
        if self.parent().brain.name is None:
            self.insertChatMessage(self.chatMessage, "Ich")
        else:
            self.insertChatMessage(self.chatMessage, self.parent().brain.name)
        
        self.ui.leNachricht.setText("")
        self.ui.leNachricht.setFocus()
        