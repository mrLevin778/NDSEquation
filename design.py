# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(600, 200)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nds_percent_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nds_percent_input.setGeometry(QtCore.QRect(60, 40, 150, 21))
        self.nds_percent_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.nds_percent_input.setText("")
        self.nds_percent_input.setMaxLength(3)
        self.nds_percent_input.setClearButtonEnabled(True)
        self.nds_percent_input.setObjectName("nds_percent_input")
        self.summa_input = QtWidgets.QLineEdit(self.centralwidget)
        self.summa_input.setGeometry(QtCore.QRect(60, 90, 150, 21))
        self.summa_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.summa_input.setText("")
        self.summa_input.setClearButtonEnabled(True)
        self.summa_input.setObjectName("summa_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 140, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 105, 16))
        self.label_2.setObjectName("label_2")
        self.minus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_btn.setGeometry(QtCore.QRect(60, 120, 150, 32))
        self.minus_btn.setObjectName("minus_btn")
        self.plus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_btn.setGeometry(QtCore.QRect(60, 160, 150, 32))
        self.plus_btn.setObjectName("plus_btn")
        self.result_summ_main = QtWidgets.QLineEdit(self.centralwidget)
        self.result_summ_main.setGeometry(QtCore.QRect(300, 85, 200, 21))
        self.result_summ_main.setClearButtonEnabled(True)
        self.result_summ_main.setObjectName("result_summ_main")
        self.result_summ = QtWidgets.QLineEdit(self.centralwidget)
        self.result_summ.setGeometry(QtCore.QRect(300, 140, 200, 21))
        self.result_summ.setClearButtonEnabled(True)
        self.result_summ.setObjectName("result_summ")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 60, 140, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 115, 140, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчёт НДС"))
        self.label.setText(_translate("MainWindow", "Введите ставку НДС:"))
        self.label_2.setText(_translate("MainWindow", "Введите сумму:"))
        self.minus_btn.setText(_translate("MainWindow", "Выделение НДС"))
        self.plus_btn.setText(_translate("MainWindow", "Начисление НДС"))
        self.label_3.setText(_translate("MainWindow", "Ваша сумма с НДС:"))
        self.label_4.setText(_translate("MainWindow", "Сумма НДС:"))
