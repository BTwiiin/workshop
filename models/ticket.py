from database import Data

class Ticket:
    def __init__(self):
        self.conn = Data()

    def add_new_ticket(self, date, description, brand, model, status, employee):
        self.conn.add_new_ticket_query(date, description, brand, model, status, employee)

    def edit_selected_ticket(self, date, description, brand, model, employee, status, id):
        self.conn.update_ticket_query(date, description, brand, model, employee, status, id)

    def delete_selected_ticket(self, id):
        self.conn.delete_ticket_query(id)

    def add_details(self, id, description, cost, acceptance):
        self.conn.add_details(id, description, cost, acceptance)

    def add_parts(self, id, name, amount, price):
        self.conn.add_parts(id, name, amount, price, (amount*price))

    def get_details(self, id):
        return self.conn.get_estimate_details_by_ticket_id(id)

    def get_parts(self, id):
        return self.conn.get_parts_by_ticket_id(id)

    def is_ticketid_valid(self, id):
        return self.conn.find_ticket_by_id(id)