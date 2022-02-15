# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 100)
        Form.setMinimumSize(QSize(420, 100))
        Form.setMaximumSize(QSize(500, 120))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditName = QLineEdit(Form)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditPhone = QLineEdit(Form)
        self.lineEditPhone.setObjectName(u"lineEditPhone")

        self.horizontalLayout_2.addWidget(self.lineEditPhone)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButtonSend = QPushButton(Form)
        self.pushButtonSend.setObjectName(u"pushButtonSend")

        self.verticalLayout.addWidget(self.pushButtonSend)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.pushButtonSend.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

