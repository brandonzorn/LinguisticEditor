# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowoZRtAQ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(477, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.max_value_input = QSpinBox(self.centralwidget)
        self.max_value_input.setObjectName(u"max_value_input")
        self.max_value_input.setMaximum(1000)
        self.max_value_input.setValue(100)

        self.verticalLayout.addWidget(self.max_value_input)

        self.points_table = QTableWidget(self.centralwidget)
        if (self.points_table.columnCount() < 3):
            self.points_table.setColumnCount(3)
        self.points_table.setObjectName(u"points_table")
        self.points_table.setColumnCount(3)
        self.points_table.horizontalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.points_table)

        self.build_graph_button = QPushButton(self.centralwidget)
        self.build_graph_button.setObjectName(u"build_graph_button")

        self.verticalLayout.addWidget(self.build_graph_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u043e\u0439 \u0448\u043a\u0430\u043b\u044b:", None))
        self.build_graph_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
    # retranslateUi

