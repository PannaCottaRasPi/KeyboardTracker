# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 645)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"QLabel {\n"
"background:\n"
"    #f4cdd4;\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-color: white;\n"
"border-width:\n"
"    0px;\n"
"color: #bb1e10;\n"
"}\n"
"QMainWindow {background: #861a22 ;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 50, 860, 511))
        self.MainLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.KeyboardDisplay = QVBoxLayout()
        self.KeyboardDisplay.setObjectName(u"KeyboardDisplay")
        self.KeyboardDisplay.setContentsMargins(-1, -1, -1, 1)
        self.ROW1 = QHBoxLayout()
        self.ROW1.setObjectName(u"ROW1")
        self.key_Q = QLabel(self.verticalLayoutWidget_2)
        self.key_Q.setObjectName(u"key_Q")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.key_Q.sizePolicy().hasHeightForWidth())
        self.key_Q.setSizePolicy(sizePolicy1)
        self.key_Q.setMinimumSize(QSize(80, 0))
        self.key_Q.setMaximumSize(QSize(16777215, 80))
        self.key_Q.setBaseSize(QSize(40, 40))
        self.key_Q.setFrameShape(QFrame.Box)
        self.key_Q.setTextFormat(Qt.MarkdownText)
        self.key_Q.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_Q)

        self.key_W = QLabel(self.verticalLayoutWidget_2)
        self.key_W.setObjectName(u"key_W")
        sizePolicy1.setHeightForWidth(self.key_W.sizePolicy().hasHeightForWidth())
        self.key_W.setSizePolicy(sizePolicy1)
        self.key_W.setMinimumSize(QSize(80, 0))
        self.key_W.setMaximumSize(QSize(16777215, 80))
        self.key_W.setBaseSize(QSize(40, 40))
        self.key_W.setFrameShape(QFrame.Box)
        self.key_W.setTextFormat(Qt.MarkdownText)
        self.key_W.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_W)

        self.key_E = QLabel(self.verticalLayoutWidget_2)
        self.key_E.setObjectName(u"key_E")
        sizePolicy1.setHeightForWidth(self.key_E.sizePolicy().hasHeightForWidth())
        self.key_E.setSizePolicy(sizePolicy1)
        self.key_E.setMinimumSize(QSize(80, 0))
        self.key_E.setMaximumSize(QSize(16777215, 80))
        self.key_E.setBaseSize(QSize(40, 40))
        self.key_E.setFrameShape(QFrame.Box)
        self.key_E.setTextFormat(Qt.MarkdownText)
        self.key_E.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_E)

        self.key_R = QLabel(self.verticalLayoutWidget_2)
        self.key_R.setObjectName(u"key_R")
        sizePolicy1.setHeightForWidth(self.key_R.sizePolicy().hasHeightForWidth())
        self.key_R.setSizePolicy(sizePolicy1)
        self.key_R.setMinimumSize(QSize(80, 0))
        self.key_R.setMaximumSize(QSize(16777215, 80))
        self.key_R.setBaseSize(QSize(40, 40))
        self.key_R.setFrameShape(QFrame.Box)
        self.key_R.setTextFormat(Qt.MarkdownText)
        self.key_R.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_R)

        self.key_T = QLabel(self.verticalLayoutWidget_2)
        self.key_T.setObjectName(u"key_T")
        sizePolicy1.setHeightForWidth(self.key_T.sizePolicy().hasHeightForWidth())
        self.key_T.setSizePolicy(sizePolicy1)
        self.key_T.setMinimumSize(QSize(80, 0))
        self.key_T.setMaximumSize(QSize(16777215, 80))
        self.key_T.setBaseSize(QSize(40, 40))
        self.key_T.setFrameShape(QFrame.Box)
        self.key_T.setTextFormat(Qt.MarkdownText)
        self.key_T.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_T)

        self.key_Y = QLabel(self.verticalLayoutWidget_2)
        self.key_Y.setObjectName(u"key_Y")
        sizePolicy1.setHeightForWidth(self.key_Y.sizePolicy().hasHeightForWidth())
        self.key_Y.setSizePolicy(sizePolicy1)
        self.key_Y.setMinimumSize(QSize(80, 0))
        self.key_Y.setMaximumSize(QSize(16777215, 80))
        self.key_Y.setBaseSize(QSize(40, 40))
        self.key_Y.setFrameShape(QFrame.Box)
        self.key_Y.setTextFormat(Qt.MarkdownText)
        self.key_Y.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_Y)

        self.key_U = QLabel(self.verticalLayoutWidget_2)
        self.key_U.setObjectName(u"key_U")
        sizePolicy1.setHeightForWidth(self.key_U.sizePolicy().hasHeightForWidth())
        self.key_U.setSizePolicy(sizePolicy1)
        self.key_U.setMinimumSize(QSize(80, 0))
        self.key_U.setMaximumSize(QSize(16777215, 80))
        self.key_U.setBaseSize(QSize(40, 40))
        self.key_U.setFrameShape(QFrame.Box)
        self.key_U.setTextFormat(Qt.MarkdownText)
        self.key_U.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_U)

        self.key_I = QLabel(self.verticalLayoutWidget_2)
        self.key_I.setObjectName(u"key_I")
        sizePolicy1.setHeightForWidth(self.key_I.sizePolicy().hasHeightForWidth())
        self.key_I.setSizePolicy(sizePolicy1)
        self.key_I.setMinimumSize(QSize(80, 0))
        self.key_I.setMaximumSize(QSize(16777215, 80))
        self.key_I.setBaseSize(QSize(40, 40))
        self.key_I.setFrameShape(QFrame.Box)
        self.key_I.setTextFormat(Qt.MarkdownText)
        self.key_I.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_I)

        self.key_O = QLabel(self.verticalLayoutWidget_2)
        self.key_O.setObjectName(u"key_O")
        sizePolicy1.setHeightForWidth(self.key_O.sizePolicy().hasHeightForWidth())
        self.key_O.setSizePolicy(sizePolicy1)
        self.key_O.setMinimumSize(QSize(80, 0))
        self.key_O.setMaximumSize(QSize(16777215, 80))
        self.key_O.setBaseSize(QSize(40, 40))
        self.key_O.setFrameShape(QFrame.Box)
        self.key_O.setTextFormat(Qt.MarkdownText)
        self.key_O.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_O)

        self.key_P = QLabel(self.verticalLayoutWidget_2)
        self.key_P.setObjectName(u"key_P")
        sizePolicy1.setHeightForWidth(self.key_P.sizePolicy().hasHeightForWidth())
        self.key_P.setSizePolicy(sizePolicy1)
        self.key_P.setMinimumSize(QSize(80, 0))
        self.key_P.setMaximumSize(QSize(16777215, 80))
        self.key_P.setBaseSize(QSize(40, 40))
        self.key_P.setFrameShape(QFrame.Box)
        self.key_P.setTextFormat(Qt.MarkdownText)
        self.key_P.setAlignment(Qt.AlignCenter)

        self.ROW1.addWidget(self.key_P)


        self.KeyboardDisplay.addLayout(self.ROW1)

        self.ROW2 = QHBoxLayout()
        self.ROW2.setObjectName(u"ROW2")
        self.horizontalSpacerR = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ROW2.addItem(self.horizontalSpacerR)

        self.key_A = QLabel(self.verticalLayoutWidget_2)
        self.key_A.setObjectName(u"key_A")
        sizePolicy1.setHeightForWidth(self.key_A.sizePolicy().hasHeightForWidth())
        self.key_A.setSizePolicy(sizePolicy1)
        self.key_A.setMinimumSize(QSize(80, 0))
        self.key_A.setMaximumSize(QSize(16777215, 80))
        self.key_A.setBaseSize(QSize(40, 40))
        self.key_A.setFrameShape(QFrame.Box)
        self.key_A.setTextFormat(Qt.MarkdownText)
        self.key_A.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_A)

        self.key_S = QLabel(self.verticalLayoutWidget_2)
        self.key_S.setObjectName(u"key_S")
        sizePolicy1.setHeightForWidth(self.key_S.sizePolicy().hasHeightForWidth())
        self.key_S.setSizePolicy(sizePolicy1)
        self.key_S.setMinimumSize(QSize(80, 0))
        self.key_S.setMaximumSize(QSize(16777215, 80))
        self.key_S.setBaseSize(QSize(40, 40))
        self.key_S.setFrameShape(QFrame.Box)
        self.key_S.setTextFormat(Qt.MarkdownText)
        self.key_S.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_S)

        self.key_D = QLabel(self.verticalLayoutWidget_2)
        self.key_D.setObjectName(u"key_D")
        sizePolicy1.setHeightForWidth(self.key_D.sizePolicy().hasHeightForWidth())
        self.key_D.setSizePolicy(sizePolicy1)
        self.key_D.setMinimumSize(QSize(80, 0))
        self.key_D.setMaximumSize(QSize(16777215, 80))
        self.key_D.setBaseSize(QSize(40, 40))
        self.key_D.setFrameShape(QFrame.Box)
        self.key_D.setTextFormat(Qt.MarkdownText)
        self.key_D.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_D)

        self.key_F = QLabel(self.verticalLayoutWidget_2)
        self.key_F.setObjectName(u"key_F")
        sizePolicy1.setHeightForWidth(self.key_F.sizePolicy().hasHeightForWidth())
        self.key_F.setSizePolicy(sizePolicy1)
        self.key_F.setMinimumSize(QSize(80, 0))
        self.key_F.setMaximumSize(QSize(16777215, 80))
        self.key_F.setBaseSize(QSize(40, 40))
        self.key_F.setFrameShape(QFrame.Box)
        self.key_F.setTextFormat(Qt.MarkdownText)
        self.key_F.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_F)

        self.key_G = QLabel(self.verticalLayoutWidget_2)
        self.key_G.setObjectName(u"key_G")
        sizePolicy1.setHeightForWidth(self.key_G.sizePolicy().hasHeightForWidth())
        self.key_G.setSizePolicy(sizePolicy1)
        self.key_G.setMinimumSize(QSize(80, 0))
        self.key_G.setMaximumSize(QSize(16777215, 80))
        self.key_G.setBaseSize(QSize(40, 40))
        self.key_G.setFrameShape(QFrame.Box)
        self.key_G.setTextFormat(Qt.MarkdownText)
        self.key_G.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_G)

        self.key_H = QLabel(self.verticalLayoutWidget_2)
        self.key_H.setObjectName(u"key_H")
        sizePolicy1.setHeightForWidth(self.key_H.sizePolicy().hasHeightForWidth())
        self.key_H.setSizePolicy(sizePolicy1)
        self.key_H.setMinimumSize(QSize(80, 0))
        self.key_H.setMaximumSize(QSize(16777215, 80))
        self.key_H.setBaseSize(QSize(40, 40))
        self.key_H.setFrameShape(QFrame.Box)
        self.key_H.setTextFormat(Qt.MarkdownText)
        self.key_H.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_H)

        self.key_J = QLabel(self.verticalLayoutWidget_2)
        self.key_J.setObjectName(u"key_J")
        sizePolicy1.setHeightForWidth(self.key_J.sizePolicy().hasHeightForWidth())
        self.key_J.setSizePolicy(sizePolicy1)
        self.key_J.setMinimumSize(QSize(80, 0))
        self.key_J.setMaximumSize(QSize(16777215, 80))
        self.key_J.setBaseSize(QSize(40, 40))
        self.key_J.setFrameShape(QFrame.Box)
        self.key_J.setTextFormat(Qt.MarkdownText)
        self.key_J.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_J)

        self.key_K = QLabel(self.verticalLayoutWidget_2)
        self.key_K.setObjectName(u"key_K")
        sizePolicy1.setHeightForWidth(self.key_K.sizePolicy().hasHeightForWidth())
        self.key_K.setSizePolicy(sizePolicy1)
        self.key_K.setMinimumSize(QSize(80, 0))
        self.key_K.setMaximumSize(QSize(16777215, 80))
        self.key_K.setBaseSize(QSize(40, 40))
        self.key_K.setFrameShape(QFrame.Box)
        self.key_K.setTextFormat(Qt.MarkdownText)
        self.key_K.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_K)

        self.key_L = QLabel(self.verticalLayoutWidget_2)
        self.key_L.setObjectName(u"key_L")
        sizePolicy1.setHeightForWidth(self.key_L.sizePolicy().hasHeightForWidth())
        self.key_L.setSizePolicy(sizePolicy1)
        self.key_L.setMinimumSize(QSize(80, 0))
        self.key_L.setMaximumSize(QSize(16777215, 80))
        self.key_L.setBaseSize(QSize(40, 40))
        self.key_L.setFrameShape(QFrame.Box)
        self.key_L.setTextFormat(Qt.MarkdownText)
        self.key_L.setAlignment(Qt.AlignCenter)

        self.ROW2.addWidget(self.key_L)

        self.horizontalSpacer_L = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ROW2.addItem(self.horizontalSpacer_L)


        self.KeyboardDisplay.addLayout(self.ROW2)

        self.ROW3 = QHBoxLayout()
        self.ROW3.setObjectName(u"ROW3")
        self.horizontalSpacer_L_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ROW3.addItem(self.horizontalSpacer_L_2)

        self.key_Z = QLabel(self.verticalLayoutWidget_2)
        self.key_Z.setObjectName(u"key_Z")
        sizePolicy1.setHeightForWidth(self.key_Z.sizePolicy().hasHeightForWidth())
        self.key_Z.setSizePolicy(sizePolicy1)
        self.key_Z.setMinimumSize(QSize(80, 0))
        self.key_Z.setMaximumSize(QSize(16777215, 80))
        self.key_Z.setBaseSize(QSize(40, 40))
        self.key_Z.setFrameShape(QFrame.Box)
        self.key_Z.setTextFormat(Qt.MarkdownText)
        self.key_Z.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_Z)

        self.key_X = QLabel(self.verticalLayoutWidget_2)
        self.key_X.setObjectName(u"key_X")
        sizePolicy1.setHeightForWidth(self.key_X.sizePolicy().hasHeightForWidth())
        self.key_X.setSizePolicy(sizePolicy1)
        self.key_X.setMinimumSize(QSize(80, 0))
        self.key_X.setMaximumSize(QSize(16777215, 80))
        self.key_X.setBaseSize(QSize(40, 40))
        self.key_X.setFrameShape(QFrame.Box)
        self.key_X.setTextFormat(Qt.MarkdownText)
        self.key_X.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_X)

        self.key_C = QLabel(self.verticalLayoutWidget_2)
        self.key_C.setObjectName(u"key_C")
        sizePolicy1.setHeightForWidth(self.key_C.sizePolicy().hasHeightForWidth())
        self.key_C.setSizePolicy(sizePolicy1)
        self.key_C.setMinimumSize(QSize(80, 0))
        self.key_C.setMaximumSize(QSize(16777215, 80))
        self.key_C.setBaseSize(QSize(40, 40))
        self.key_C.setFrameShape(QFrame.Box)
        self.key_C.setTextFormat(Qt.MarkdownText)
        self.key_C.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_C)

        self.key_V = QLabel(self.verticalLayoutWidget_2)
        self.key_V.setObjectName(u"key_V")
        sizePolicy1.setHeightForWidth(self.key_V.sizePolicy().hasHeightForWidth())
        self.key_V.setSizePolicy(sizePolicy1)
        self.key_V.setMinimumSize(QSize(80, 0))
        self.key_V.setMaximumSize(QSize(16777215, 80))
        self.key_V.setBaseSize(QSize(40, 40))
        self.key_V.setFrameShape(QFrame.Box)
        self.key_V.setTextFormat(Qt.MarkdownText)
        self.key_V.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_V)

        self.key_B = QLabel(self.verticalLayoutWidget_2)
        self.key_B.setObjectName(u"key_B")
        sizePolicy1.setHeightForWidth(self.key_B.sizePolicy().hasHeightForWidth())
        self.key_B.setSizePolicy(sizePolicy1)
        self.key_B.setMinimumSize(QSize(80, 0))
        self.key_B.setMaximumSize(QSize(16777215, 80))
        self.key_B.setBaseSize(QSize(40, 40))
        self.key_B.setFrameShape(QFrame.Box)
        self.key_B.setTextFormat(Qt.MarkdownText)
        self.key_B.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_B)

        self.key_N = QLabel(self.verticalLayoutWidget_2)
        self.key_N.setObjectName(u"key_N")
        sizePolicy1.setHeightForWidth(self.key_N.sizePolicy().hasHeightForWidth())
        self.key_N.setSizePolicy(sizePolicy1)
        self.key_N.setMinimumSize(QSize(80, 0))
        self.key_N.setMaximumSize(QSize(16777215, 80))
        self.key_N.setBaseSize(QSize(40, 40))
        self.key_N.setFrameShape(QFrame.Box)
        self.key_N.setTextFormat(Qt.MarkdownText)
        self.key_N.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_N)

        self.key_M = QLabel(self.verticalLayoutWidget_2)
        self.key_M.setObjectName(u"key_M")
        sizePolicy1.setHeightForWidth(self.key_M.sizePolicy().hasHeightForWidth())
        self.key_M.setSizePolicy(sizePolicy1)
        self.key_M.setMinimumSize(QSize(80, 0))
        self.key_M.setMaximumSize(QSize(16777215, 80))
        self.key_M.setBaseSize(QSize(40, 40))
        self.key_M.setFrameShape(QFrame.Box)
        self.key_M.setTextFormat(Qt.MarkdownText)
        self.key_M.setAlignment(Qt.AlignCenter)

        self.ROW3.addWidget(self.key_M)

        self.horizontalSpacer_R = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ROW3.addItem(self.horizontalSpacer_R)


        self.KeyboardDisplay.addLayout(self.ROW3)

        self.ROW4 = QHBoxLayout()
        self.ROW4.setObjectName(u"ROW4")
        self.key_SPACE = QLabel(self.verticalLayoutWidget_2)
        self.key_SPACE.setObjectName(u"key_SPACE")
        sizePolicy1.setHeightForWidth(self.key_SPACE.sizePolicy().hasHeightForWidth())
        self.key_SPACE.setSizePolicy(sizePolicy1)
        self.key_SPACE.setMinimumSize(QSize(80, 0))
        self.key_SPACE.setMaximumSize(QSize(16777215, 80))
        self.key_SPACE.setBaseSize(QSize(40, 40))
        self.key_SPACE.setFrameShape(QFrame.Box)
        self.key_SPACE.setTextFormat(Qt.MarkdownText)
        self.key_SPACE.setAlignment(Qt.AlignCenter)

        self.ROW4.addWidget(self.key_SPACE)


        self.KeyboardDisplay.addLayout(self.ROW4)


        self.MainLayout.addLayout(self.KeyboardDisplay)

        self.graphicsView = PlotWidget(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.MainLayout.addWidget(self.graphicsView)

        self.MainLayout.setStretch(0, 70)
        self.MainLayout.setStretch(1, 30)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.key_Q.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_W.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_E.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_R.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_T.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_Y.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_U.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_I.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_O.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_P.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_A.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_S.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_D.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_F.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_G.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_H.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_J.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_K.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_L.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_Z.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_X.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_C.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_V.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_B.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_N.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_M.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Key</p><p>0</p></body></html>", None))
        self.key_SPACE.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SPACE</p></body></html>", None))
    # retranslateUi

