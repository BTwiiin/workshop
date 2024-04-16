from database import Data

class Employee:
    def __init__(self):
        self.conn = Data()

    def add_new_employee(self, name, surname, wage):
        self.conn.add_new_employee_query(name, surname, wage)

    def delete_selected_employee(self, id):
        self.conn.delete_employee_query(id)

    def find_employee_bool(self, id):
        return self.conn.find_employee_query(id)
