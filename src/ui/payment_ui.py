# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 149)
        Dialog.setStyleSheet("#error_lbl {\n"
"    color: red;\n"
"}")
        self.cash_rb = QtWidgets.QRadioButton(Dialog)
        self.cash_rb.setGeometry(QtCore.QRect(39, 32, 82, 17))
        self.cash_rb.setObjectName("cash_rb")
        self.credit_rb = QtWidgets.QRadioButton(Dialog)
        self.credit_rb.setGeometry(QtCore.QRect(39, 52, 82, 17))
        self.credit_rb.setObjectName("credit_rb")
        self.check_rb = QtWidgets.QRadioButton(Dialog)
        self.check_rb.setGeometry(QtCore.QRect(39, 72, 82, 17))
        self.check_rb.setObjectName("check_rb")
        self.print_btn = QtWidgets.QPushButton(Dialog)
        self.print_btn.setGeometry(QtCore.QRect(205, 60, 183, 35))
        self.print_btn.setObjectName("print_btn")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(245, 30, 46, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.total_lbl = QtWidgets.QLabel(Dialog)
        self.total_lbl.setGeometry(QtCore.QRect(298, 30, 86, 16))
        self.total_lbl.setText("")
        self.total_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_lbl.setObjectName("total_lbl")
        self.error_lbl = QtWidgets.QLabel(Dialog)
        self.error_lbl.setGeometry(QtCore.QRect(20, 98, 165, 16))
        self.error_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.error_lbl.setObjectName("error_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cash_rb.setText(_translate("Dialog", "Cash"))
        self.credit_rb.setText(_translate("Dialog", "Credit Card"))
        self.check_rb.setText(_translate("Dialog", "Check"))
        self.print_btn.setText(_translate("Dialog", "Print Receipt"))
        self.label_17.setText(_translate("Dialog", "Total"))
        self.error_lbl.setText(_translate("Dialog", "Please select a payment method."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

