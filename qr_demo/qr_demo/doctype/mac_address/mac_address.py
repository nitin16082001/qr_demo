# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt
# import get_mac_address 
# import frappe
# from frappe.model.document import Document

# class Macaddress(Document):
# 	@frappe.whitelist()
# 	def address(self):
# 		mac = address.get_mac_address()
# 		return mac
# import uuid
# import frappe
# from frappe.model.document import Document

# class Macaddress(Document):
#     @frappe.whitelist()
# 	def address():
#     	mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
#     	return mac
# 		mac_address = address()
# 		frapee.msgprint(str(mac_address) )

import uuid
import frappe
from frappe.model.document import Document

class Macaddress(Document):
    @frappe.whitelist()
    def address(self):
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
        self.mac_address=mac
        frappe.msgprint(str(mac))
        return mac

        
