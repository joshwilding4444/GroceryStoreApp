from ui import smith_ui, login_ui, payment_ui
from classes import employee, product

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QSplashScreen, QProgressBar, QDialog
import sys
from decimal import Decimal, ROUND_HALF_UP

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
        self.setWindowTitle("Smith's Grocery")
        self.setWindowIcon(QtGui.QIcon('48x48.png'))
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        self.get_employees() # populate employee list
        self.current_employee = None

        self.launch_login_dialog()

        # Connections
        self.log_out_btn.clicked.connect(self.launch_login_dialog)

        #########################################
        # Manage Employee Initializing
        #########################################
        self.me_new_employee_b = False

        # Connections
        self.me_create_new_employee_btn.clicked.connect(self.handle_create_new_employee)
        self.me_delete_employee_btn.clicked.connect(self.handle_delete_employee)
        self.me_update_employee_btn.clicked.connect(self.handle_update_employee)
        self.me_employee_listview.clicked.connect(self.populate_employee_info)

        #########################################
        # Manage Product Initializing
        #########################################
        self.temporary_product_list = []
        self.temporary_product_list.append(product.Product("Apple", 1, 100, .25, 1.51, False, 0))
        self.temporary_product_list.append(product.Product("Orange", 2, 100, .35, 1.92, False, 0))
        self.current_product = None
        self.mp_new_product_b = False

        # Connections
        self.mp_search_btn.clicked.connect(self.get_product)
        self.mp_add_btn.clicked.connect(self.handle_add_new_product)
        self.mp_delete_btn.clicked.connect(self.handle_delete_product)
        self.mp_update_btn.clicked.connect(self.handle_update_employee)

        #########################################
        # Begin Checkout Initializing
        #########################################
        self.reset_checkout()
        self.receipt_names = []
        self.receipt_quantity = []
        self.receipt_price = []
        self.receipt_other = []
        self.cents = Decimal('.01')
        self.tax_rate = Decimal(.047)
        self.subtotal = Decimal(0.0)
        self.tax = Decimal(0.0)
        self.total = Decimal(0.0)

        # Connections
        self.bc_begin_checkout_btn.clicked.connect(self.begin_checkout)
        self.bc_search_btn.clicked.connect(self.bc_get_product)
        self.bc_barcode_search_field.returnPressed.connect(self.bc_get_product)
        self.bc_quantity_sbox.valueChanged.connect(self.calculate_item_subtotal)
        self.bc_weight_sbox.valueChanged.connect(self.calculate_item_subtotal)
        self.bc_add_btn.clicked.connect(self.handle_add_item)
        self.bc_remove_btn.clicked.connect(self.handle_remove_item)
        # self.bc_get_payment_btn.clicked.connect()
        self.bc_receipt_listview.clicked.connect(self.enable_remove_btn)
        self.bc_cancel_btn.clicked.connect(self.cancel_transaction)
        # self.bc_weight_sbox.returnPressed.connect(self.handle_add_item)

    def launch_login_dialog(self):
        self.tabWidget.clear()
        self.employee_id_lbl.setText("")
        self.employee_name_lbl.setText("")
        self.login_dialog = LoginDialog(self)
        self.login_dialog.exec_()

    def get_employees(self):
        "Get employee list from database and read it into self.employee_list"
        print("Calling DB - Populating Employee List")
        self.employee_list = []

        # loop through what we get back from DB

        # Temporary hardcoded-data
        self.employee_list.append(employee.Employee("Jim Smith", 1, "1", 0))
        self.employee_list.append(employee.Employee("Samantha Williams", 2, "1", 1))

    def display_tabs(self):
        "Displays tabs based on user role. Admins have access to Manage Employees/Manage Products/Begin Checkout"
        """Cashiers only have access to Begin Checkout"""
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
        "Read employee list into Manage Employees List View"
        self.me_employee_list_model = QStandardItemModel(self.me_employee_listview)

        for employee in self.employee_list:
            item = QStandardItem(str(employee.employee_id) + ' ' + employee.employee_name)
            self.me_employee_list_model.appendRow(item)

        self.me_employee_listview.setModel(self.me_employee_list_model)

    def handle_create_new_employee(self):
        "Creates a new employee in the database"
        self.me_new_employee_b = True
        print("Calling DB - Getting New Employee ID")
        # self.me_id_lbl.setText()
        self.me_name_field.setText("")
        self.me_password_field.setText("")
        self.get_employees() # recreate employee list
        self.populate_me_employee_list_view() # reload employee list view

    def handle_update_employee(self):
        "Updates employee info"
        if self.me_new_employee_b:
            print("Calling DB") #update new employee
            self.me_new_employee_b = False
        else:
            print("Calling DB - Update Current Employee ") #update current employee
        self.get_employees() # recreate employee list
        self.populate_me_employee_list_view() # reload employee list view

    def handle_delete_employee(self):
        "Delete employee from database"
        # TODO: confirmation dialog
        print("Calling DB - Delete Employee") # delete current employee
        self.me_id_lbl.setText("")
        self.me_name_field.setText("")
        self.me_password_field.setText("")
        self.me_employee_gbox.setEnabled(False)
        self.me_delete_employee_btn.setEnabled(False)
        self.get_employees() # recreate employee list
        self.populate_me_employee_list_view() # reload employee list view

    def populate_employee_info(self):
        "Displays selected employee info"
        self.me_employee_gbox.setEnabled(True)
        self.me_delete_employee_btn.setEnabled(True)
        self.me_update_employee_btn.setEnabled(True)
        self.edit_employee = self.employee_list[self.me_employee_listview.selectedIndexes()[0].row()]
        print(str(self.me_employee_listview.selectedIndexes()[0].row()))
        print(str(self.edit_employee.employee_name))
        self.me_id_lbl.setText(str(self.edit_employee.employee_id))
        self.me_name_field.setText(self.edit_employee.employee_name)
        self.me_password_field.setText(self.edit_employee.employee_password)
        self.me_role_cbox.setCurrentIndex(int(self.edit_employee.role))


#########################################
# Manage Product Functions
#########################################
    def get_product(self):
        "Get prodcut info from Database"
        print("Calling DB - Getting Product Info " + self.mp_barcode_search_field.text())
        for product in self.temporary_product_list:
            if self.mp_barcode_search_field.text() == str(product.barcode):
                self.mp_delete_btn.setEnabled(True)
                self.mp_update_btn.setEnabled(True)
                self.mp_current_product = product
                self.mp_product_gbox.setEnabled(True)
                self.mp_name_field.setText(product.name)
                self.mp_barcode_field.setText(str(product.barcode))
                self.mp_available_units_field.setText(str(product.available))
                self.mp_price_field.setText(str(product.price))
                self.mp_customer_price_field.setText(str(product.customer_price))
                if product.weigh_b:
                    self.mp_weigh_rb.setChecked(True)
                else:
                    self.mp_quantity_rb.setChecked(True)
                self.mp_provider_field.setText(str(product.provider))
                self.mp_barcode_search_field.setText("")

    def handle_add_new_product(self):
        "Clears product fields so new info can be added"
        self.mp_new_product_b = True
        self.mp_product_gbox.setEnabled(True)
        self.mp_delete_btn.setEnabled(True)
        self.mp_update_btn.setEnabled(True)
        self.mp_name_field.setText("")
        self.mp_barcode_field.setText("")
        self.mp_available_units_field.setText("")
        self.mp_price_field.setText("")
        self.mp_customer_price_field.setText("")
        self.mp_quantity_rb.setChecked(True)
        self.mp_provider_field.setText("")
        self.mp_current_product = product.Product(self.mp_name_field.text(), self.mp_barcode_field.text(),
                                                  self.mp_available_units_field.text(),
                                                  self.mp_price_field.text(), self.mp_customer_price_field.text(),
                                                  self.mp_quantity_rb.isChecked(), self.mp_provider_field.text())

    def handle_update_product(self):
        "Updates employee info"
        if self.mp_new_product_b:
            print("Calling DB - Update Add a New Product")  # update new product
            self.mp_new_product_b = False
        else:
            print("Calling DB - Update Product")  # update current product

    def handle_delete_product(self):
        "Delete employee from database"
        # TODO: confirmation dialog
        print("Calling DB - Delete Product " + str(self.mp_current_product.barcode))  # delete current product
        self.mp_name_field.setText("")
        self.mp_barcode_field.setText("")
        self.mp_available_units_field.setText("")
        self.mp_price_field.setText("")
        self.mp_customer_price_field.setText("")
        self.mp_quantity_rb.setChecked(True)
        self.mp_provider_field.setText("")
        self.mp_product_gbox.setEnabled(False)
        self.mp_delete_btn.setEnabled(False)
        self.mp_update_btn.setEnabled(False)


#########################################
# Begin Checkout Functions
#########################################
    def begin_checkout(self):
        "Begin transaction and show checkout screen"
        self.bc_begin_checkout_btn.setHidden(True)
        self.bc_checkout_frame.setHidden(False)
        self.bc_cancel_btn.setEnabled(True)
        self.co_product_list = []
        self.co_quantity = []

    def cancel_transaction(self):
        "Cancels transaction and sets checkouts to initialization"
        self.bc_begin_checkout_btn.setHidden(False)
        self.bc_checkout_frame.setHidden(True)
        self.bc_cancel_btn.setEnabled(False)

        self.reset_checkout()
        self.receipt_names = []
        self.receipt_quantity = []
        self.receipt_price = []
        self.receipt_other = []
        self.cents = Decimal('.01')
        self.tax_rate = Decimal(.047)
        self.subtotal = Decimal(0.0)
        self.tax = Decimal(0.0)
        self.total = Decimal(0.0)

        # reset listview
        self.bc_receipt_list_model = QStandardItemModel(self.bc_receipt_listview)
        self.bc_receipt_listview.setModel(self.bc_receipt_list_model)

        # Update totals labels
        self.bc_r_subtotal_lbl.setText('$' + str(self.subtotal) + ".00")
        self.bc_tax_lbl.setText('$' + str(self.tax) + ".00")
        self.bc_total_lbl.setText('$' + str(self.total) + ".00")

        self.bc_quantity_frame.setEnabled(False)
        self.current_product = None
        self.bc_item_info_frame.setEnabled(False)
        self.bc_name_lbl.setText("")
        self.bc_barcode_lbl.setText("")
        self.bc_available_lbl.setText("")
        self.bc_price_lbl.setText("")
        self.bc_weight_sbox.setEnabled(False)
        self.bc_quantity_sbox.setEnabled(False)
        self.bc_quantity_lbl.setEnabled(False)
        self.bc_weight_lbl.setEnabled(False)
        self.bc_provider_lbl.setText("")
        self.bc_subtotal_lbl.setText("")
        self.bc_barcode_search_field.setText("")
        self.bc_btn_frame.setEnabled(False)

    def enable_remove_btn(self):
        self.bc_remove_btn.setEnabled(True)

    def reset_checkout(self):
        "Show checkout frame"
        self.bc_checkout_frame.setHidden(True)

    def bc_get_product(self):
        "Get product info from database and populate labels"
        print("Calling DB - Product Lookup")
        for product in self.temporary_product_list:
            if self.bc_barcode_search_field.text() == str(product.barcode):
                self.bc_quantity_sbox.setValue(0)
                self.bc_weight_sbox.setValue(0.00)
                self.bc_quantity_frame.setEnabled(True)
                self.current_product = product
                self.bc_item_info_frame.setEnabled(True)
                self.bc_name_lbl.setText(product.name)
                self.bc_barcode_lbl.setText(str(product.barcode))
                self.bc_available_lbl.setText(str(product.available))
                self.bc_price_lbl.setText(str(product.customer_price))
                if product.weigh_b:
                    self.bc_weight_sbox.setEnabled(True)
                    self.bc_quantity_sbox.setEnabled(False)
                    self.bc_quantity_lbl.setEnabled(False)
                    self.bc_weight_lbl.setEnabled(True)
                else:
                    self.bc_weight_lbl.setEnabled(False)
                    self.bc_weight_sbox.setEnabled(False)
                    self.bc_quantity_sbox.setEnabled(True)
                    self.bc_quantity_lbl.setEnabled(True)
                self.bc_provider_lbl.setText(str(product.provider))
                self.calculate_item_subtotal()
                self.bc_barcode_search_field.setText("")
                self.bc_btn_frame.setEnabled(True)

    def calculate_item_subtotal(self):
        if self.current_product.weigh_b:
            self.bc_subtotal_lbl.setText(str(Decimal(self.bc_weight_sbox.value() * self.current_product.customer_price)).quantize(self.cents, ROUND_HALF_UP))
        else:
            self.bc_subtotal_lbl.setText(str(Decimal(self.bc_quantity_sbox.value() * self.current_product.customer_price).quantize(self.cents, ROUND_HALF_UP)))

    def handle_add_item(self):
        "Add item to receipt and lists"
        # Store barcode, quantity/weight, price for receipt storage
        self.receipt_names.append(self.bc_barcode_lbl.text())
        if self.current_product.weigh_b:
            self.receipt_quantity.append(self.bc_weight_sbox.value())
        else:
            self.receipt_quantity.append(self.bc_quantity_sbox.value())
        self.receipt_price.append(self.bc_price_lbl.text())

        self.update_receipt()

    def update_receipt(self):
        if not self.bc_receipt_frame.isEnabled():
            self.bc_receipt_list_model = QStandardItemModel(self.bc_receipt_listview)
        self.bc_receipt_frame.setEnabled(True)

        if self.current_product.weigh_b:
            item = QStandardItem(self.bc_name_lbl.text() + ' (' + str(self.bc_weight_sbox.value()) + ')\n$' + str(Decimal(Decimal(self.bc_weight_sbox.value()) * Decimal(self.bc_price_lbl.text())).quantize(self.cents, ROUND_HALF_UP)))
        else:
            item = QStandardItem(self.bc_name_lbl.text() + ' (' + str(self.bc_quantity_sbox.value()) + ')\n$' + str(Decimal(int(self.bc_quantity_sbox.value()) * Decimal(self.bc_price_lbl.text())).quantize(self.cents, ROUND_HALF_UP)))
        # item.setCheckable(True)

        self.bc_receipt_list_model.appendRow(item)

        self.bc_receipt_listview.setModel(self.bc_receipt_list_model)

        # Calculate totals
        self.subtotal += Decimal(int(self.bc_quantity_sbox.value()) * Decimal(self.bc_price_lbl.text())).quantize(self.cents, ROUND_HALF_UP)
        self.tax += Decimal((int(self.bc_quantity_sbox.value()) * Decimal(self.bc_price_lbl.text())) * self.tax_rate).quantize(self.cents, ROUND_HALF_UP)
        self.total = self.subtotal + self.tax

        # Update totals labels
        self.bc_r_subtotal_lbl.setText('$' + str(self.subtotal))
        self.bc_tax_lbl.setText('$' + str(self.tax))
        self.bc_total_lbl.setText('$' + str(self.total))

    def handle_remove_item(self):
        "Removes selected item from listview and receipt lists"
        print("Before Item Removal")
        print(str(self.receipt_names))
        print(str(self.receipt_quantity))
        print(str(self.receipt_price))

        try:
            row = self.bc_receipt_listview.selectedIndexes()[0].row()

            # UPDATE TOTALS
            self.subtotal -= Decimal(int(self.receipt_quantity[row]) * self.receipt_price[row]).quantize(self.cents, ROUND_HALF_UP)
            self.tax -= Decimal((int(self.receipt_quantity[row]) * Decimal(self.receipt_price[row])) * self.tax_rate).quantize(self.cents, ROUND_HALF_UP)
            self.total -= Decimal(int(self.receipt_quantity[row]) * self.receipt_price[row]).quantize(self.cents, ROUND_HALF_UP) + Decimal((int(self.receipt_quantity[row]) * Decimal(self.receipt_price[row])) * self.tax_rate).quantize(self.cents, ROUND_HALF_UP)

            # Update totals labels
            self.bc_r_subtotal_lbl.setText('$' + str(self.subtotal))
            self.bc_tax_lbl.setText('$' + str(self.tax))
            self.bc_total_lbl.setText('$' + str(self.total))

            self.bc_receipt_list_model.removeRow(row)
            self.receipt_names.pop(row)
            self.receipt_quantity.pop(row)
            self.receipt_price.pop(row)

            print("After Item Removal")
            print(str(self.receipt_names))
            print(str(self.receipt_quantity))
            print(str(self.receipt_price))


        except IndexError: # If no items are selected
            print("Index Error - Please select an Item")


app = QApplication([])


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.show()
    app.exec_()
