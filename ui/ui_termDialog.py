# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'termDialogMycjHE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.term_count = QSpinBox(Dialog)
        self.term_count.setObjectName(u"term_count")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.term_count)

        self.Label_2 = QLabel(Dialog)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Label_2)

        self.var_name = QLineEdit(Dialog)
        self.var_name.setObjectName(u"var_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.var_name)

        self.Label = QLabel(Dialog)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)


        self.verticalLayout.addLayout(self.formLayout)

        self.term_inputs = QVBoxLayout()
        self.term_inputs.setObjectName(u"term_inputs")

        self.verticalLayout.addLayout(self.term_inputs)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.build_button = QPushButton(Dialog)
        self.build_button.setObjectName(u"build_button")

        self.verticalLayout_2.addWidget(self.build_button)

        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout_2.addWidget(self.save_button)

        self.load_button = QPushButton(Dialog)
        self.load_button.setObjectName(u"load_button")

        self.verticalLayout_2.addWidget(self.load_button)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0435\u0440\u043c\u043e\u0432:", None))
        self.Label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439:", None))
        self.build_button.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.load_button.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
    # retranslateUi

