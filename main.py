import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QPdfWriter, QPageSize, QPainter


from models.employee import Employee
from models.ticket import Ticket
from view.add_details import Ui_Details_Dialog
from view.add_parts import Ui_Part_Dialog
from view.choose_ticket import Ui_Save_Dialog
from view.new_employee import Ui_Dialog_employee
from view.ui_main import Ui_MainWindow
from view.new_ticket import Ui_Dialog


class Workshop(QMainWindow):
    def __init__(self):
        super(Workshop, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ticket_manager = Ticket()
        self.employee_manager = Employee()
        self.set_update_tickets()
        self.set_update_employees()

        self.ui.new_ticket_button.clicked.connect(self.open_new_ticket_window)
        self.ui.edit_ticket_button.clicked.connect(self.open_new_ticket_window)
        self.ui.delete_ticket_button.clicked.connect(self.delete_selected_ticket)
        self.ui.save_pdf_button.clicked.connect(self.open_new_save_window)

        self.ui.add_employee.clicked.connect(self.open_new_employee_window)
        self.ui.delete_employee.clicked.connect(self.delete_selected_employee)
        self.ui.detail_ticket_button.clicked.connect(self.open_new_detail_window)
        self.ui.parts_ticket_button.clicked.connect(self.open_new_part_window)

        selection_model = self.ui.tableView.selectionModel()
        selection_model.selectionChanged.connect(self.update_button_styles_if_not_selected)
        self.update_button_styles_if_not_selected()

    def set_update_tickets(self):
        self.model = QSqlTableModel(self)
        self.partsModel = QSqlTableModel(self)
        self.estimatesModel = QSqlTableModel(self)
        self.model.setTable('tickets')
        self.partsModel.setTable('parts')
        self.estimatesModel.setTable('estimates')
        self.model.select()
        self.partsModel.select()
        self.estimatesModel.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView_3.setModel(self.estimatesModel)
        self.ui.tableView_4.setModel(self.partsModel)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.update_button_styles_if_not_selected)
        self.update_button_styles_if_not_selected()

    def set_update_employees(self):
        self.employeesModel = QSqlTableModel(self)
        self.employeesModel.setTable('employees')
        self.employeesModel.select()
        self.ui.tableView_2.setModel(self.employeesModel)

    def update_button_styles_if_not_selected(self):
        has_data_in_tickets = self.model.rowCount() > 0

        has_ticket_selection = self.ui.tableView.selectionModel().hasSelection() and has_data_in_tickets

        btn_style = ("QPushButton{ color: rgb(255, 255, 255); " 
                            "background-color:rgba(255,255,255,30);"
                            "border: 1px solid rgba(255,255,255,40);"
                            "border-radius:7px;"
                            "width: 230;"
                            "height: 50;"
                            "}") if has_ticket_selection else ("QPushButton{ color: rgb(255, 255, 255); "
                                                        "background-color:rgba(255,255,255,30);")

        self.ui.edit_ticket_button.setStyleSheet(btn_style)
        self.ui.delete_ticket_button.setStyleSheet(btn_style)
        self.ui.detail_ticket_button.setStyleSheet(btn_style)
        self.ui.parts_ticket_button.setStyleSheet(btn_style)

    def open_ticket_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)

    def open_employee_window(self):
        self.new_window_employee = QtWidgets.QDialog()
        self.ui_window_employee = Ui_Dialog_employee()
        self.ui_window_employee.setupUi(self.new_window_employee)

    def open_detail_window(self):
        self.new_window_detail = QtWidgets.QDialog()
        self.ui_window_detail = Ui_Details_Dialog()
        self.ui_window_detail.setupUi(self.new_window_detail)

    def open_part_window(self):
        self.new_window_part = QtWidgets.QDialog()
        self.ui_window_part = Ui_Part_Dialog()
        self.ui_window_part.setupUi(self.new_window_part)

    def open_save_window(self):
        self.new_window_save = QtWidgets.QDialog()
        self.ui_window_save = Ui_Save_Dialog()
        self.ui_window_save.setupUi(self.new_window_save)

    def are_ticket_details_valid(self):

        details = {
            'Date': self.ui_window.ticket_date.text(),
            'Description': self.ui_window.ticket_description.text(),
            'Brand': self.ui_window.ticket_brand.text(),
            'Model': self.ui_window.ticket_model.text(),
            'Status': self.ui_window.ticket_status.currentText(),
        }

        # Check each detail for being empty
        for key, value in details.items():
            if not value.strip():  # Checks if the string is empty after removing leading/trailing whitespace
                QtWidgets.QMessageBox.warning(self, "Missing Information", f"{key} is required.")
                self.new_window.close()
                return False

        employee_id_str = self.ui_window.ticket_employee.text().strip()
        try:
            employee_id = int(employee_id_str)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Employee must be a valid number.")
            return False

        if not self.employee_manager.find_employee_bool(employee_id):
            QtWidgets.QMessageBox.warning(self, "Invalid Employee", "No such employee exists.")
            return False

        details['Employee'] = employee_id
        return details

    def are_employee_details_valid(self):
        details = {
            'Name': self.ui_window_employee.employee_name.text(),
            'Surname': self.ui_window_employee.employee_surname.text(),
        }

        for key, value in details.items():
            if not value.strip():
                QtWidgets.QMessageBox.warning(self, "Missing Information", f"{key} is required.")
                self.new_window_employee.close()
                return False

        wage = self.ui_window_employee.employee_wage.text().strip()
        try:
            wage = float(wage)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Wage must be a valid number.")
            return False
        details['Wage'] = wage
        return details

    def are_tickets_details_valid(self):
        details = {
            'Description': self.ui_window_detail.details_description.text(),
        }

        for key, value in details.items():
            if not value.strip():
                QtWidgets.QMessageBox.warning(self, "Missing Information", f"{key} is required.")
                self.new_window_detail.close()
                return False
        details['Cost'] = self.ui_window_detail.estimated_cost.value()
        if self.ui_window_detail.acceptance_status.isChecked():
            details['Acceptance'] = 'Accepted'
        else:
            details['Acceptance'] = 'Not Accepted'
        return details

    def are_tickets_parts_valid(self):
        details = {
            'Name': self.ui_window_part.part_name.text(),
        }

        for key, value in details.items():
            if not value.strip():
                QtWidgets.QMessageBox.warning(self, "Missing Information", f"{key} is required.")
                self.new_window_detail.close()
                return False

        parts_price = self.ui_window_part.part_price.text().strip()
        try:
            price = float(parts_price)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Employee must be a valid number.")
            return False

        if price < 0:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Must be positive number.")
            return False
        details['Amount'] = self.ui_window_part.part_amount.value()
        details['Price'] = price
        return details

    def open_new_ticket_window(self):
        sender = self.sender()
        if sender.text() == "New ticket":
            # If the action is to add a new ticket, create and show the dialog immediately.
            self.open_ticket_window()
            self.ui_window.save_ticket_button.clicked.connect(self.add_new_ticket)
            self.new_window.show()
        else:
            indexes = self.ui.tableView.selectedIndexes()
            if not indexes:
                QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select a ticket to edit.")
                return

            index = indexes[0]
            id = str(self.ui.tableView.model().data(index))
            self.open_ticket_window()
            self.ui_window.save_ticket_button.clicked.connect(lambda: self.edit_selected_ticket(id))
            self.new_window.show()

    def open_new_employee_window(self):
        self.open_employee_window()
        self.ui_window_employee.save_employee_button.clicked.connect(self.add_new_employee)
        self.new_window_employee.show()

    def open_new_detail_window(self):
        indexes = self.ui.tableView.selectedIndexes()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select a ticket to edit.")
            return

        index = indexes[0]
        id = str(self.ui.tableView.model().data(index))
        self.open_detail_window()
        self.ui_window_detail.save_details_ticket_button.clicked.connect(lambda: self.add_ticket_details(id))
        self.new_window_detail.show()

    def open_new_part_window(self):
        indexes = self.ui.tableView.selectedIndexes()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select a ticket.")
            return

        index = indexes[0]
        id = str(self.ui.tableView.model().data(index))
        self.open_part_window()
        self.ui_window_part.save_part_ticket_button.clicked.connect(lambda: self.add_ticket_parts(id))
        self.new_window_part.show()

    def open_new_save_window(self):
        self.open_save_window()
        self.ui_window_save.save_pdf_ticket_button.clicked.connect(self.save_to_pdf)
        self.new_window_save.show()

    def add_new_employee(self):
        details = self.are_employee_details_valid()
        if not details:
            return

        self.employee_manager.add_new_employee(details['Name'], details['Surname'], details['Wage'])
        self.set_update_employees()
        self.new_window_employee.close()

    def add_new_ticket(self):
        details = self.are_ticket_details_valid()
        if not details:
            return

        self.ticket_manager.add_new_ticket(details['Date'], details['Description'], details['Brand'],
                                           details['Model'], details['Employee'], details['Status'])
        self.set_update_tickets()
        self.new_window.close()

    def edit_selected_ticket(self, id):

        details = self.are_ticket_details_valid()
        if not details:
            return

        self.ticket_manager.edit_selected_ticket(details['Date'], details['Description'], details['Brand'],
                                           details['Model'], details['Employee'], details['Status'], id)
        self.set_update_tickets()
        self.new_window.close()

    def delete_selected_ticket(self):
        indexes = self.ui.tableView.selectedIndexes()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select a ticket to delete.")
            return

        index = indexes[0]
        id = str(self.ui.tableView.model().data(index))

        self.ticket_manager.delete_selected_ticket(id)
        self.set_update_tickets()

    def delete_selected_employee(self):
        indexes = self.ui.tableView_2.selectedIndexes()
        if not indexes:
            QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select an employee to delete.")
            return

        index = indexes[0]
        id = str(self.ui.tableView_2.model().data(index))

        self.employee_manager.delete_selected_employee(id)
        self.set_update_employees()

    def add_ticket_details(self, id):
        details = self.are_tickets_details_valid()
        if not details:
            return

        self.ticket_manager.add_details(id, details['Description'], details['Cost'], details['Acceptance'])
        self.new_window_detail.close()
        self.set_update_tickets()

    def add_ticket_parts(self, id):
        details = self.are_tickets_parts_valid()
        if not details:
            return

        self.ticket_manager.add_parts(id, details['Name'], details['Amount'], details['Price'])
        self.new_window_part.close()
        self.set_update_tickets()

    def save_to_pdf(self, id):
        id = self.ui_window_save.ticketId_tosave.value()
        if not self.ticket_manager.is_ticketid_valid(id):
            QtWidgets.QMessageBox.warning(self, "Missing Information", f"No such ticketId: {id}.")
            self.new_window_save.close()
            return

        self.new_window_save.close()

        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save PDF",
            os.path.expanduser("~"),  # Start in the user's home directory
            "PDF Files (*.pdf)"
        )

        # Check if the user provided a file path or canceled the dialog
        if not file_path:
            print("File save cancelled.")
            return

        writer = QPdfWriter(file_path)
        writer.setPageSize(QPageSize(QSize(800, 400)))
        painter = QPainter(writer)
        estimates = self.ticket_manager.get_details(id)
        parts = self.ticket_manager.get_parts(id)

        # Starting positions for the text
        x = 100
        y = 100
        line_height = 200

        # Write Estimates
        painter.drawText(x, y, f"Estimates for Ticket ID: {id}")
        y += line_height
        painter.drawText(x, y, f"Description: {estimates[2]}")
        y += line_height
        painter.drawText(x, y, f"Expected Cost: {estimates[3]}")
        y += line_height
        painter.drawText(x, y, f"Accepted by Client: {estimates[4]}")
        y += line_height * 4

        painter.drawText(x, y, "Parts:")
        y += line_height
        for part in parts:
            painter.drawText(x, y,
                             f"Name: {part['Name']}, Amount: {part['Amount']}, Unit Price: {part['UnitPrice']}, Total Price: {part['TotalPrice']}")
            y += line_height

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Workshop()
    window.show()

    sys.exit(app.exec())
