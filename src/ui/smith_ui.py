# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smith.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1114, 771)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(12, 39, 1091, 686))
        self.tabWidget.setObjectName("tabWidget")
        self.manage_employees_tab = QtWidgets.QWidget()
        self.manage_employees_tab.setObjectName("manage_employees_tab")
        self.me_employee_listview = QtWidgets.QListView(self.manage_employees_tab)
        self.me_employee_listview.setGeometry(QtCore.QRect(16, 20, 256, 629))
        self.me_employee_listview.setObjectName("me_employee_listview")
        self.me_employee_gbox = QtWidgets.QGroupBox(self.manage_employees_tab)
        self.me_employee_gbox.setEnabled(False)
        self.me_employee_gbox.setGeometry(QtCore.QRect(288, 15, 509, 193))
        self.me_employee_gbox.setObjectName("me_employee_gbox")
        self.me_delete_employee_btn = QtWidgets.QPushButton(self.me_employee_gbox)
        self.me_delete_employee_btn.setGeometry(QtCore.QRect(298, 69, 183, 35))
        self.me_delete_employee_btn.setObjectName("me_delete_employee_btn")
        self.label_4 = QtWidgets.QLabel(self.me_employee_gbox)
        self.label_4.setGeometry(QtCore.QRect(14, 29, 89, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.me_update_employee_btn = QtWidgets.QPushButton(self.me_employee_gbox)
        self.me_update_employee_btn.setGeometry(QtCore.QRect(72, 133, 183, 35))
        self.me_update_employee_btn.setObjectName("me_update_employee_btn")
        self.label_5 = QtWidgets.QLabel(self.me_employee_gbox)
        self.label_5.setGeometry(QtCore.QRect(14, 61, 89, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.me_employee_gbox)
        self.label_6.setGeometry(QtCore.QRect(14, 95, 89, 13))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.me_password_field = QtWidgets.QLineEdit(self.me_employee_gbox)
        self.me_password_field.setGeometry(QtCore.QRect(109, 91, 161, 20))
        self.me_password_field.setObjectName("me_password_field")
        self.me_name_field = QtWidgets.QLineEdit(self.me_employee_gbox)
        self.me_name_field.setGeometry(QtCore.QRect(109, 57, 161, 20))
        self.me_name_field.setObjectName("me_name_field")
        self.me_id_lbl = QtWidgets.QLabel(self.me_employee_gbox)
        self.me_id_lbl.setGeometry(QtCore.QRect(110, 29, 89, 13))
        self.me_id_lbl.setText("")
        self.me_id_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.me_id_lbl.setObjectName("me_id_lbl")
        self.me_create_new_employee_btn = QtWidgets.QPushButton(self.manage_employees_tab)
        self.me_create_new_employee_btn.setGeometry(QtCore.QRect(585, 40, 183, 35))
        self.me_create_new_employee_btn.setObjectName("me_create_new_employee_btn")
        self.tabWidget.addTab(self.manage_employees_tab, "")
        self.manage_products_tab = QtWidgets.QWidget()
        self.manage_products_tab.setObjectName("manage_products_tab")
        self.label_33 = QtWidgets.QLabel(self.manage_products_tab)
        self.label_33.setGeometry(QtCore.QRect(16, 42, 89, 13))
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.mp_barcode_search_field = QtWidgets.QLineEdit(self.manage_products_tab)
        self.mp_barcode_search_field.setGeometry(QtCore.QRect(112, 38, 161, 20))
        self.mp_barcode_search_field.setObjectName("mp_barcode_search_field")
        self.mp_search_btn = QtWidgets.QPushButton(self.manage_products_tab)
        self.mp_search_btn.setGeometry(QtCore.QRect(68, 75, 183, 35))
        self.mp_search_btn.setObjectName("mp_search_btn")
        self.mp_product_gbox = QtWidgets.QGroupBox(self.manage_products_tab)
        self.mp_product_gbox.setEnabled(False)
        self.mp_product_gbox.setGeometry(QtCore.QRect(342, 18, 535, 297))
        self.mp_product_gbox.setObjectName("mp_product_gbox")
        self.mp_delete_btn = QtWidgets.QPushButton(self.mp_product_gbox)
        self.mp_delete_btn.setGeometry(QtCore.QRect(300, 68, 183, 35))
        self.mp_delete_btn.setObjectName("mp_delete_btn")
        self.mp_provider_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_provider_field.setGeometry(QtCore.QRect(107, 192, 161, 20))
        self.mp_provider_field.setObjectName("mp_provider_field")
        self.mp_name_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_name_field.setGeometry(QtCore.QRect(107, 24, 161, 20))
        self.mp_name_field.setObjectName("mp_name_field")
        self.mp_update_btn = QtWidgets.QPushButton(self.mp_product_gbox)
        self.mp_update_btn.setGeometry(QtCore.QRect(80, 236, 183, 35))
        self.mp_update_btn.setObjectName("mp_update_btn")
        self.label_9 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_9.setGeometry(QtCore.QRect(11, 94, 89, 13))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_15.setGeometry(QtCore.QRect(11, 162, 89, 13))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.mp_available_units_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_available_units_field.setGeometry(QtCore.QRect(107, 90, 161, 20))
        self.mp_available_units_field.setObjectName("mp_available_units_field")
        self.label_13 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_13.setGeometry(QtCore.QRect(11, 196, 89, 13))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.mp_price_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_price_field.setGeometry(QtCore.QRect(107, 126, 161, 20))
        self.mp_price_field.setObjectName("mp_price_field")
        self.label_12 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_12.setGeometry(QtCore.QRect(11, 130, 89, 13))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.mp_customer_price_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_customer_price_field.setGeometry(QtCore.QRect(107, 158, 161, 20))
        self.mp_customer_price_field.setObjectName("mp_customer_price_field")
        self.mp_barcode_field = QtWidgets.QLineEdit(self.mp_product_gbox)
        self.mp_barcode_field.setGeometry(QtCore.QRect(107, 56, 161, 20))
        self.mp_barcode_field.setObjectName("mp_barcode_field")
        self.label_11 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_11.setGeometry(QtCore.QRect(11, 28, 89, 13))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.mp_product_gbox)
        self.label_10.setGeometry(QtCore.QRect(11, 60, 89, 13))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.mp_add_btn = QtWidgets.QPushButton(self.manage_products_tab)
        self.mp_add_btn.setGeometry(QtCore.QRect(642, 40, 183, 35))
        self.mp_add_btn.setObjectName("mp_add_btn")
        self.tabWidget.addTab(self.manage_products_tab, "")
        self.begin_checkout_tab = QtWidgets.QWidget()
        self.begin_checkout_tab.setObjectName("begin_checkout_tab")
        self.bc_begin_checkout_btn = QtWidgets.QPushButton(self.begin_checkout_tab)
        self.bc_begin_checkout_btn.setGeometry(QtCore.QRect(465, 200, 183, 35))
        self.bc_begin_checkout_btn.setObjectName("bc_begin_checkout_btn")
        self.bc_checkout_frame = QtWidgets.QFrame(self.begin_checkout_tab)
        self.bc_checkout_frame.setGeometry(QtCore.QRect(10, 10, 1066, 646))
        self.bc_checkout_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_checkout_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_checkout_frame.setObjectName("bc_checkout_frame")
        self.bc_btn_frame = QtWidgets.QFrame(self.bc_checkout_frame)
        self.bc_btn_frame.setEnabled(False)
        self.bc_btn_frame.setGeometry(QtCore.QRect(79, 370, 221, 156))
        self.bc_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_btn_frame.setObjectName("bc_btn_frame")
        self.bc_remove_btn = QtWidgets.QPushButton(self.bc_btn_frame)
        self.bc_remove_btn.setGeometry(QtCore.QRect(20, 55, 183, 35))
        self.bc_remove_btn.setObjectName("bc_remove_btn")
        self.bc_get_payment_btn = QtWidgets.QPushButton(self.bc_btn_frame)
        self.bc_get_payment_btn.setGeometry(QtCore.QRect(20, 110, 183, 35))
        self.bc_get_payment_btn.setObjectName("bc_get_payment_btn")
        self.bc_add_btn = QtWidgets.QPushButton(self.bc_btn_frame)
        self.bc_add_btn.setGeometry(QtCore.QRect(20, 15, 183, 35))
        self.bc_add_btn.setObjectName("bc_add_btn")
        self.bc_item_info_frame = QtWidgets.QFrame(self.bc_checkout_frame)
        self.bc_item_info_frame.setEnabled(False)
        self.bc_item_info_frame.setGeometry(QtCore.QRect(9, 190, 371, 176))
        self.bc_item_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_item_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_item_info_frame.setObjectName("bc_item_info_frame")
        self.label_7 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_7.setGeometry(QtCore.QRect(12, 15, 141, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.bc_item_info_frame)
        self.line.setGeometry(QtCore.QRect(20, 115, 346, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bc_available_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_available_lbl.setGeometry(QtCore.QRect(165, 55, 213, 16))
        self.bc_available_lbl.setText("")
        self.bc_available_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_available_lbl.setObjectName("bc_available_lbl")
        self.bc_name_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_name_lbl.setGeometry(QtCore.QRect(165, 15, 213, 16))
        self.bc_name_lbl.setText("")
        self.bc_name_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_name_lbl.setObjectName("bc_name_lbl")
        self.label_21 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_21.setGeometry(QtCore.QRect(12, 75, 141, 16))
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.bc_barcode_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_barcode_lbl.setGeometry(QtCore.QRect(165, 35, 213, 16))
        self.bc_barcode_lbl.setText("")
        self.bc_barcode_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_barcode_lbl.setObjectName("bc_barcode_lbl")
        self.label_8 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_8.setGeometry(QtCore.QRect(12, 35, 141, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.bc_subtotal_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_subtotal_lbl.setGeometry(QtCore.QRect(165, 130, 213, 16))
        self.bc_subtotal_lbl.setText("")
        self.bc_subtotal_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_subtotal_lbl.setObjectName("bc_subtotal_lbl")
        self.bc_provider_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_provider_lbl.setGeometry(QtCore.QRect(165, 95, 213, 16))
        self.bc_provider_lbl.setText("")
        self.bc_provider_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_provider_lbl.setObjectName("bc_provider_lbl")
        self.label_14 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_14.setGeometry(QtCore.QRect(12, 55, 141, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_36 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_36.setGeometry(QtCore.QRect(12, 95, 141, 16))
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.bc_price_lbl = QtWidgets.QLabel(self.bc_item_info_frame)
        self.bc_price_lbl.setGeometry(QtCore.QRect(165, 75, 213, 16))
        self.bc_price_lbl.setText("")
        self.bc_price_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_price_lbl.setObjectName("bc_price_lbl")
        self.label_43 = QtWidgets.QLabel(self.bc_item_info_frame)
        self.label_43.setGeometry(QtCore.QRect(12, 130, 141, 16))
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.bc_search_frame = QtWidgets.QFrame(self.bc_checkout_frame)
        self.bc_search_frame.setGeometry(QtCore.QRect(9, 25, 301, 161))
        self.bc_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_search_frame.setObjectName("bc_search_frame")
        self.bc_barcode_search_field = QtWidgets.QLineEdit(self.bc_search_frame)
        self.bc_barcode_search_field.setGeometry(QtCore.QRect(110, 6, 161, 20))
        self.bc_barcode_search_field.setObjectName("bc_barcode_search_field")
        self.label = QtWidgets.QLabel(self.bc_search_frame)
        self.label.setGeometry(QtCore.QRect(15, 10, 89, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.bc_search_frame)
        self.label_3.setGeometry(QtCore.QRect(15, 135, 89, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.bc_search_frame)
        self.label_2.setGeometry(QtCore.QRect(15, 100, 89, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.bc_quantity_sbox = QtWidgets.QSpinBox(self.bc_search_frame)
        self.bc_quantity_sbox.setGeometry(QtCore.QRect(110, 96, 42, 22))
        self.bc_quantity_sbox.setProperty("value", 1)
        self.bc_quantity_sbox.setObjectName("bc_quantity_sbox")
        self.bc_search_btn = QtWidgets.QPushButton(self.bc_search_frame)
        self.bc_search_btn.setGeometry(QtCore.QRect(65, 40, 183, 35))
        self.bc_search_btn.setObjectName("bc_search_btn")
        self.bc_weight_sbox = QtWidgets.QDoubleSpinBox(self.bc_search_frame)
        self.bc_weight_sbox.setGeometry(QtCore.QRect(110, 130, 62, 22))
        self.bc_weight_sbox.setSingleStep(0.1)
        self.bc_weight_sbox.setObjectName("bc_weight_sbox")
        self.bc_receipt_frame = QtWidgets.QFrame(self.bc_checkout_frame)
        self.bc_receipt_frame.setEnabled(False)
        self.bc_receipt_frame.setGeometry(QtCore.QRect(610, 0, 456, 641))
        self.bc_receipt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_receipt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_receipt_frame.setObjectName("bc_receipt_frame")
        self.bc_total_lbl = QtWidgets.QLabel(self.bc_receipt_frame)
        self.bc_total_lbl.setGeometry(QtCore.QRect(359, 620, 86, 16))
        self.bc_total_lbl.setText("")
        self.bc_total_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bc_total_lbl.setObjectName("bc_total_lbl")
        self.bc_subtotal_lbl_2 = QtWidgets.QLabel(self.bc_receipt_frame)
        self.bc_subtotal_lbl_2.setGeometry(QtCore.QRect(359, 580, 86, 16))
        self.bc_subtotal_lbl_2.setText("")
        self.bc_subtotal_lbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bc_subtotal_lbl_2.setObjectName("bc_subtotal_lbl_2")
        self.label_18 = QtWidgets.QLabel(self.bc_receipt_frame)
        self.label_18.setGeometry(QtCore.QRect(295, 580, 56, 16))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.bc_receipt_frame)
        self.label_17.setGeometry(QtCore.QRect(295, 620, 56, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.bc_receipt_listview = QtWidgets.QListView(self.bc_receipt_frame)
        self.bc_receipt_listview.setGeometry(QtCore.QRect(5, 5, 446, 571))
        self.bc_receipt_listview.setObjectName("bc_receipt_listview")
        self.bc_tax_lbl = QtWidgets.QLabel(self.bc_receipt_frame)
        self.bc_tax_lbl.setGeometry(QtCore.QRect(359, 600, 86, 16))
        self.bc_tax_lbl.setText("")
        self.bc_tax_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bc_tax_lbl.setObjectName("bc_tax_lbl")
        self.label_16 = QtWidgets.QLabel(self.bc_receipt_frame)
        self.label_16.setGeometry(QtCore.QRect(295, 600, 56, 16))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.bc_checkout_frame.raise_()
        self.bc_begin_checkout_btn.raise_()
        self.tabWidget.addTab(self.begin_checkout_tab, "")
        self.employee_id_lbl = QtWidgets.QLabel(self.centralwidget)
        self.employee_id_lbl.setGeometry(QtCore.QRect(15, 10, 66, 21))
        self.employee_id_lbl.setObjectName("employee_id_lbl")
        self.employee_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.employee_name_lbl.setGeometry(QtCore.QRect(85, 10, 236, 21))
        self.employee_name_lbl.setObjectName("employee_name_lbl")
        self.log_out_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_btn.setGeometry(QtCore.QRect(919, 10, 183, 35))
        self.log_out_btn.setObjectName("log_out_btn")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.me_employee_gbox.setTitle(_translate("main_window", "Employee"))
        self.me_delete_employee_btn.setText(_translate("main_window", "Delete Employee"))
        self.label_4.setText(_translate("main_window", "Employee ID"))
        self.me_update_employee_btn.setText(_translate("main_window", "Update Employee"))
        self.label_5.setText(_translate("main_window", "Employee Name"))
        self.label_6.setText(_translate("main_window", "Password"))
        self.me_create_new_employee_btn.setText(_translate("main_window", "Create a New Employee"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manage_employees_tab), _translate("main_window", "Manage Employees"))
        self.label_33.setText(_translate("main_window", "Barcode Search"))
        self.mp_search_btn.setText(_translate("main_window", "Search"))
        self.mp_product_gbox.setTitle(_translate("main_window", "Product Information"))
        self.mp_delete_btn.setText(_translate("main_window", "Delete Product"))
        self.mp_update_btn.setText(_translate("main_window", "Update Product"))
        self.label_9.setText(_translate("main_window", "Available Units"))
        self.label_15.setText(_translate("main_window", "Customer Price"))
        self.label_13.setText(_translate("main_window", "Provider"))
        self.label_12.setText(_translate("main_window", "Price"))
        self.label_11.setText(_translate("main_window", "Procuct Name"))
        self.label_10.setText(_translate("main_window", "Barcode"))
        self.mp_add_btn.setText(_translate("main_window", "Add a New Product"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manage_products_tab), _translate("main_window", "Manage Products"))
        self.bc_begin_checkout_btn.setText(_translate("main_window", "Begin Checkout"))
        self.bc_remove_btn.setText(_translate("main_window", "Remove Item"))
        self.bc_get_payment_btn.setText(_translate("main_window", "Get Payment"))
        self.bc_add_btn.setText(_translate("main_window", "Add Item"))
        self.label_7.setText(_translate("main_window", "Item Name"))
        self.label_21.setText(_translate("main_window", "Price per Unit"))
        self.label_8.setText(_translate("main_window", "Barcode Number"))
        self.label_14.setText(_translate("main_window", "Number of Available Units"))
        self.label_36.setText(_translate("main_window", "Provider"))
        self.label_43.setText(_translate("main_window", "Item subtotal"))
        self.label.setText(_translate("main_window", "Item Barcode"))
        self.label_3.setText(_translate("main_window", "Weight"))
        self.label_2.setText(_translate("main_window", "Quantity"))
        self.bc_search_btn.setText(_translate("main_window", "Search"))
        self.label_18.setText(_translate("main_window", "Subtotal"))
        self.label_17.setText(_translate("main_window", "Total"))
        self.label_16.setText(_translate("main_window", "Tax"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.begin_checkout_tab), _translate("main_window", "Begin Checkout"))
        self.employee_id_lbl.setText(_translate("main_window", "Employee ID"))
        self.employee_name_lbl.setText(_translate("main_window", "Employee Name"))
        self.log_out_btn.setText(_translate("main_window", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

