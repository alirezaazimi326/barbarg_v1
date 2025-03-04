import frappe
from frappe.model.document import Document

class DriversLog(Document):
    def validate(self):
        if not self.timestamp:
            self.timestamp = frappe.utils.now_datetime() 