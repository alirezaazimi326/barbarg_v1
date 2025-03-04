# Copyright (c) 2024, Barbarg and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class Drivers(Document):
    def before_insert(self):
        frappe.log_error("Before Insert Called", "Debug")
        
    def before_save(self):
        frappe.log_error("Before Save Called", "Debug")
        
    def validate(self):
        frappe.log_error("Validate Called", "Debug")
        try:
            # Log all document fields for debugging
            doc_data = {
                "user_name": self.user_name,
                "password": "***",  # Hide password in logs
                "plate_info": {
                    "left": self.plate_left,
                    "char": self.plate_char,
                    "middle": self.plate_middle,
                    "right": self.plate_right
                }
            }
            frappe.log_error(f"Document Data: {json.dumps(doc_data, indent=2)}", "Debug Data")
            
            if not self.user_name:
                frappe.throw("User Name is required")
            if not self.password:
                frappe.throw("Password is required")
                
            self.generate_full_plate()
            
        except Exception as e:
            error_msg = f"Error in validate: {str(e)}"
            frappe.log_error(error_msg, "Drivers Validation Error")
            frappe.throw(error_msg)
    
    def generate_full_plate(self):
        try:
            if all([self.plate_left, self.plate_char, self.plate_middle, self.plate_right]):
                # Format: 88 | 333 ذ 22 (IR code | 3 digits | letter | 2 digits)
                self.full_plate = f"{self.plate_right} | {self.plate_middle} {self.plate_char} {self.plate_left}"
                frappe.log_error(f"Plate generated: {self.full_plate}", "Debug")
            else:
                frappe.log_error("Some plate fields are empty", "Debug")
        except Exception as e:
            error_msg = f"Error in generate_full_plate: {str(e)}"
            frappe.log_error(error_msg, "Plate Generation Error")
            raise e