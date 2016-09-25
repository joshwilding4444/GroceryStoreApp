from ui import smith_ui, login_ui, payment_ui
from classes import employee, product

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QSplashScreen, QProgressBar, QDialog
import sys

# Get exception codes
# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


class LoginDialog(QtWidgets.QDialog, login_ui.Ui_login_dialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.main_window = parent
        self.error_lbl.setText("")
        self.employee_id_field.setFocus()

        # connections
        self.sign_in_btn.clicked.connect(self.handle_sign_in_btn)
        self.employee_id_field.textChanged.connect(self.clear_error_lbl)
        self.password_field.textChanged.connect(self.clear_error_lbl)

    def handle_sign_in_btn(self):
        for employee in self.main_window.employee_list:
            print(str(employee.employee_id))
            if self.employee_id_field.text() == str(employee.employee_id) and self.password_field.text() == employee.employee_password:
                self.main_window.employee_id_lbl.setText(str(employee.employee_id))
                self.main_window.employee_name_lbl.setText(employee.employee_name)
                self.main_window.current_employee = employee
                self.main_window.display_tabs()
                self.close()
            else:
                self.error_lbl.setText("Incorrect ID or Password")

    def clear_error_lbl(self):
        self.error_lbl.setText("")




class MainWindow(QMainWindow, smith_ui.Ui_main_window):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.setupUi(self)

        # Setup
        # self.screenShape = QtWidgets.QDesktopWidget().screenGeometry()
        # self.setGeometry(0, 0, self.screenShape.width() * .7, (self.screenShape.height() - 40) * .9)
        self.setWindowTitle("Smith's Grocery")
        self.setWindowIcon(QtGui.QIcon('48x48.png'))
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        ## Hide widgets until log in
        # self.tabWidget.setHidden(True)
        # self.employee_id_lbl.setText("")
        # self.employee_name_lbl.setText("")
        # self.log_out_btn.setHidden(True)

        self.get_employees()
        self.current_employee = None

        self.launch_login_dialog()

        # # Reset tabs/Display according to user role
        # self.display_tabs()

        # Connections
        self.log_out_btn.clicked.connect(self.launch_login_dialog)

        #########################################
        # Manage Employee Initializing
        #########################################
        # Connections
        # self.me_create_new_employee_btn.clicked.connect()
        # self.me_delete_employee_btn.clicked.connect()
        # self.me_update_employee_btn.clicked.connect()
        # self.me_employee_listview.clicked.connect()

        #########################################
        # Manage Product Initializing
        #########################################
        self.temporary_product_list = []
        self.temporary_product_list.append(product.Product("Apple", 1, 100, .25, 1.51, 0, False))
        self.temporary_product_list.append(product.Product("Orange", 2, 100, .35, 1.92, 0, False))
        self.current_product = None
        # Connections
        self.mp_search_btn.clicked.connect(self.get_product)
        # self.mp_add_btn.clicked.connect()
        # self.mp_delete_btn.clicked.connect()
        # self.mp_update_btn.clicked.connect()


        #########################################
        # Begin Checkout Initializing
        #########################################
        self.reset_checkout()

        # Connections
        self.bc_begin_checkout_btn.clicked.connect(self.begin_checkout)
        self.bc_search_btn.clicked.connect(self.bc_get_product)
        self.bc_quantity_sbox.valueChanged.connect(self.calculate_item_subtotal)
        self.bc_weight_sbox.valueChanged.connect(self.calculate_item_subtotal)
        # self.bc_add_btn.clicked.connect()
        # self.bc_remove_btn.clicked.connect()
        # self.bc_get_payment_btn.clicked.connect()


    def launch_login_dialog(self):
        self.tabWidget.clear()
        self.employee_id_lbl.setText("")
        self.employee_name_lbl.setText("")
        self.login_dialog = LoginDialog(self)
        self.login_dialog.exec_()

    def get_employees(self):
        print("Calling DB")
        self.employee_list = []
        # loop through what we get back from DB
        self.employee_list.append(employee.Employee("Jim Smith", 1, "1", 0))
        self.employee_list.append(employee.Employee("Samantha Williams", 2, "1", 1))

    def display_tabs(self):
        self.tabWidget.clear()

        if self.current_employee.role == 0:
            self.tabWidget.insertTab(0, self.begin_checkout_tab, "Begin Checkout")

            self.tabWidget.insertTab(0, self.manage_products_tab, "Manage Products")


            self.tabWidget.insertTab(0, self.manage_employees_tab, "Manage Employees")
            self.populate_me_employee_list_view()

            self.tabWidget.setCurrentIndex(0)
        elif self.current_employee.role == 1:
            self.tabWidget.insertTab(0, self.begin_checkout_tab, "Begin Checkout")
            self.tabWidget.setCurrentIndex(0)

#########################################
# Manage Employee Functions
#########################################
    def populate_me_employee_list_view(self):
        print("Hello")
        self.me_employee_list_model = QStandardItemModel(self.me_employee_listview)

        for employee in self.employee_list:
            item = QStandardItem(str(employee.employee_id) + ' ' + employee.employee_name)
            self.me_employee_list_model.appendRow(item)

        self.me_employee_listview.setModel(self.me_employee_list_model)

    def reset_checkout(self):
        self.bc_checkout_frame.setHidden(True)


#########################################
# Manage Product Functions
#########################################
    def get_product(self):
        print("Calling DB")
        for product in self.temporary_product_list:
            if self.mp_barcode_search_field.text() == str(product.barcode):
                self.mp_product_gbox.setEnabled(True)
                self.mp_name_field.setText(product.name)
                self.mp_barcode_field.setText(str(product.barcode))
                self.mp_available_units_field.setText(str(product.available))
                self.mp_price_field.setText(str(product.price))
                self.mp_customer_price_field.setText(str(product.customer_price))
                # if product.weigh_b:
                #     self.weigh_rb.setChecked(True)
                # else:
                #     self.quantity_rb.setChecked(True)
                self.mp_provider_field.setText(str(product.provider))
                self.mp_barcode_search_field.setText("")



#########################################
# Begin Checkout Functions
#########################################
    def begin_checkout(self):
        self.bc_begin_checkout_btn.setHidden(True)
        self.bc_checkout_frame.setHidden(False)
        self.co_product_list = []
        self.co_quantity = []

    def bc_get_product(self):
        print("Calling DB")
        for product in self.temporary_product_list:
            if self.bc_barcode_search_field.text() == str(product.barcode):
                self.current_product = product
                self.bc_item_info_frame.setEnabled(True)
                self.bc_name_lbl.setText(product.name)
                self.bc_barcode_lbl.setText(str(product.barcode))
                self.bc_available_lbl.setText(str(product.available))
                self.bc_price_lbl.setText(str(product.price))
                if product.weigh_b:
                    self.bc_weigh_sbox.setEnabled(True)
                    self.bc_quantity_sbox.setEnabled(False)
                else:
                    self.bc_weight_sbox.setEnabled(False)
                    self.bc_quantity_sbox.setEnabled(True)
                self.bc_provider_lbl.setText(str(product.provider))
                self.calculate_item_subtotal()
                self.bc_barcode_search_field.setText("")

    def calculate_item_subtotal(self):
        if self.current_product.weigh_b:
            self.bc_subtotal_lbl.setText(str(self.bc_weight_sbox.value() * self.current_product.customer_price))
        else:
            self.bc_subtotal_lbl.setText(str(round(self.bc_quantity_sbox.value() * self.current_product.customer_price, 2)))

app = QApplication([])


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.show()
    app.exec_()
