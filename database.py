from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('workshop.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        query.exec("CREATE TABLE IF NOT EXISTS employees (ID integer primary key AUTOINCREMENT,"
                   " Given_Name VARCHAR(20), Surname VARCHAR(20), Wage FLOAT)")

        query.exec("CREATE TABLE IF NOT EXISTS tickets (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Brand VARCHAR(20), Model VARCHAR(20), ProblemDescription TEXT, EmployeeAssigned integer,"
                   " Status VARCHAR(20), FOREIGN KEY (EmployeeAssigned) REFERENCES employees(ID))")

        query.exec("CREATE TABLE IF NOT EXISTS time_slots (ID INTEGER PRIMARY KEY AUTOINCREMENT, StartTime DATETIME,"
                   "EndTime DATETIME, Hours INTEGER)")

        query.exec("CREATE TABLE employee_time_slots ( EmployeeID INTEGER, TimeSlotID INTEGER, "
                   "OREIGN KEY (EmployeeID) REFERENCES employees(ID), FOREIGN KEY (TimeSlotID) REFERENCES time_slots(ID),"
                   "PRIMARY KEY (EmployeeID, TimeSlotID))")

        query.exec("CREATE TABLE IF NOT EXISTS estimates (ID INTEGER PRIMARY KEY AUTOINCREMENT, TicketID INTEGER, "
                   "Description TEXT, ExpectedCost REAL, AcceptedByClient TEXT,"
                   "FOREIGN KEY (TicketID) REFERENCES tickets (ID))")

        query.exec("CREATE TABLE IF NOT EXISTS parts ( ID INTEGER PRIMARY KEY AUTOINCREMENT, TicketID INTEGER,"
                   "Name TEXT, Amount REAL, UnitPrice REAL, TotalPrice REAL, "
                   "FOREIGN KEY (TicketID) REFERENCES tickets (ID))")

        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_ticket_query(self, date, problemDescription, brand, model, employeeAssigned, status):
        sql_query = ("INSERT INTO tickets (Date, ProblemDescription, Brand, Model,"
                     " EmployeeAssigned, Status) VALUES (?, ?, ?, ?, ?, ?)")
        self.execute_query_with_params(sql_query, [date, problemDescription, brand,
                                                   model, employeeAssigned, status])

    def update_ticket_query(self, date, problemDescription, brand, model, employeeAssigned, status, id):
        sql_query = ("UPDATE tickets SET Date=?, ProblemDescription=?, Brand=?, Model=?,"
                     " EmployeeAssigned=?, Status=? WHERE ID=?")
        self.execute_query_with_params(sql_query, [date, problemDescription, brand,
                                                   model, employeeAssigned, status, id])

    def delete_ticket_query(self, id):
        sql_query = "DELETE FROM tickets WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])
        sql_query = ("DELETE FROM estimates WHERE TicketID=?")
        self.execute_query_with_params(sql_query, [id])
        sql_query = ("DELETE FROM parts WHERE TicketID=?")
        self.execute_query_with_params(sql_query, [id])

    def add_new_employee_query(self, name, surname, wage):
        sql_query = ("INSERT INTO employees (Given_Name, Surname, Wage) VALUES (?, ?, ?)")
        self.execute_query_with_params(sql_query, [name, surname, wage])

    def delete_employee_query(self, id):
        sql_query = "DELETE FROM employees WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def find_employee_query(self, id):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM employees WHERE ID = ?")
        query.addBindValue(id)
        query.exec_()

        if query.next():
            count = query.value(0)
            return count > 0
        else:
            return False

    def add_details(self, id, description, cost, acceptance):
        if self.find_details_query(id):
            sql_query = ("UPDATE estimates SET Description=?, ExpectedCost=?, AcceptedByClient=?"
                         " WHERE TicketID=?")
            self.execute_query_with_params(sql_query, [description, cost, acceptance, id])
        else:
            sql_query = ("INSERT INTO estimates (TicketID, Description, ExpectedCost, AcceptedByClient) VALUES (?, ?, ?, ?)")
            self.execute_query_with_params(sql_query, [id, description, cost, acceptance])

    def find_details_query(self, id):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM estimates WHERE TicketID = ?")
        query.addBindValue(id)
        query.exec_()

        if query.next():
            count = query.value(0)
            return count > 0
        else:
            return False

    def add_parts(self, id, name, amount, price, total):
        sql_query = ("INSERT INTO parts (TicketID, Name, Amount, UnitPrice, TotalPrice) VALUES (?, ?, ?, ?, ?)")
        self.execute_query_with_params(sql_query, [id, name, amount, price, total])

    def get_estimate_details_by_ticket_id(self, ticket_id):
        query = QtSql.QSqlQuery()
        query.prepare(
            "SELECT ID, TicketID, Description, ExpectedCost, AcceptedByClient FROM estimates WHERE TicketID = :ticketID")
        query.bindValue(":ticketID", ticket_id)

        if query.exec_() and query.next():
            result = (
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4)
            )
            return result
        else:
            return None

    def get_parts_by_ticket_id(self, ticket_id):
        results = []
        query = QtSql.QSqlQuery()
        query.prepare(
            "SELECT ID, TicketID, Name, Amount, UnitPrice, TotalPrice FROM parts WHERE TicketID = :ticketID")
        query.bindValue(":ticketID", ticket_id)
        if query.exec_():
            while query.next():
                result = {
                    'ID': query.value(0),
                    'TicketID': query.value(1),
                    'Name': query.value(2),
                    'Amount': query.value(3),
                    'UnitPrice': query.value(4),
                    'TotalPrice': query.value(5)
                }
                results.append(result)
            return results

    def find_ticket_by_id(self, ticket_id):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM tickets WHERE ID = :ticketID")
        query.bindValue(":ticketID", ticket_id)
        if query.exec_() and query.next():
            count = query.value(0)
            return count > 0