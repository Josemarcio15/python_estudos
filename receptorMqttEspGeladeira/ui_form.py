# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(496, 600)
        self.solicitar_dados = QPushButton(Widget)
        self.solicitar_dados.setObjectName(u"solicitar_dados")
        self.solicitar_dados.setGeometry(QRect(140, 120, 171, 24))
        self.enviar_parametros = QPushButton(Widget)
        self.enviar_parametros.setObjectName(u"enviar_parametros")
        self.enviar_parametros.setGeometry(QRect(130, 390, 171, 24))
        self.tempminina = QLineEdit(Widget)
        self.tempminina.setObjectName(u"tempminina")
        self.tempminina.setGeometry(QRect(140, 300, 113, 24))
        self.tempmaxima = QLineEdit(Widget)
        self.tempmaxima.setObjectName(u"tempmaxima")
        self.tempmaxima.setGeometry(QRect(140, 340, 113, 24))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(56, 303, 80, 16))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(56, 344, 80, 16))
        self.parminima = QLabel(Widget)
        self.parminima.setObjectName(u"parminima")
        self.parminima.setGeometry(QRect(140, 160, 49, 16))
        self.parmaximo = QLabel(Widget)
        self.parmaximo.setObjectName(u"parmaximo")
        self.parmaximo.setGeometry(QRect(140, 190, 49, 16))
        self.compressor = QLabel(Widget)
        self.compressor.setObjectName(u"compressor")
        self.compressor.setGeometry(QRect(140, 220, 49, 16))
        self.tempatual = QLabel(Widget)
        self.tempatual.setObjectName(u"tempatual")
        self.tempatual.setGeometry(QRect(140, 240, 49, 16))
        self.label1 = QLabel(Widget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(80, 160, 49, 16))
        self.label2 = QLabel(Widget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(80, 190, 49, 16))
        self.label3 = QLabel(Widget)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(60, 220, 70, 16))
        self.label4 = QLabel(Widget)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(64, 240, 70, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.solicitar_dados.setText(QCoreApplication.translate("Widget", u"Solicitar Dados", None))
        self.enviar_parametros.setText(QCoreApplication.translate("Widget", u"Enviar Parametros", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Temp minima", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Temp maxima", None))
        self.parminima.setText(QCoreApplication.translate("Widget", u"n/a", None))
        self.parmaximo.setText(QCoreApplication.translate("Widget", u"n/a", None))
        self.compressor.setText(QCoreApplication.translate("Widget", u"n/a", None))
        self.tempatual.setText(QCoreApplication.translate("Widget", u"n/a", None))
        self.label1.setText(QCoreApplication.translate("Widget", u"minima", None))
        self.label2.setText(QCoreApplication.translate("Widget", u"maxima", None))
        self.label3.setText(QCoreApplication.translate("Widget", u"Compressor", None))
        self.label4.setText(QCoreApplication.translate("Widget", u"Temp Atual", None))
    # retranslateUi

