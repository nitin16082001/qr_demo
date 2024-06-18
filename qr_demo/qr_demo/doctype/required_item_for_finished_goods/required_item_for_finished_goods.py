# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RequiredItemForFinishedGoods(Document):
	@frappe.whitelist()
	def append_user_entry(self):
		count=1
		for value in self.get("entry_catalog"):
				if(self.qr_code_data==value.qr_code_data and self.stage==value.stage):
					count=0
		if(count):
			self.append(
					"entry_catalog", {
						"customer_name":self.customer_name,
						"qr_code_data":self.qr_code_data,
						"finished_item":self.finished_item,
						"actual_stage":self.actual_stage,
						"stage":self.stage,
						"quantity":self.quantity,
						"date":self.date,
						"time":self.time,
						"stage_name":self.stage_name,
						"user":self.user,
						"shift":self.shift,
						"shift_incharge":self.shift_incharge,
						"pcb_side":self.pcb_side,
						"process_count":True
					}
				)
			for value in self.get("entry_catalog"):
				if(value.stage=="1" and value.process_count):	
					self.process_one=self.process_one+1
					value.process_count=False
				if(value.stage=="2" and value.process_count):
					self.process_two=self.process_two+1
					value.process_count=False
				elif(value.stage=="3" and value.process_count):
					self.process_three=self.process_three+1
					value.process_count=False
				elif(value.stage=="4" and value.process_count):
					self.process_four=self.process_four+1
					value.process_count=False
				elif(value.stage=="5" and value.process_count):
					self.process_five=self.process_five+1
					value.process_count=False
				elif(value.stage=="6" and value.process_count):
					self.process_six=self.process_six+1
					value.process_count=False
				elif(value.stage=="7" and value.process_count):
					self.process_seven=self.process_seven+1
					value.process_count=False
				elif(value.stage=="8" and value.process_count):
					self.process_eight=self.process_eight+1
					value.process_count=False
				elif(value.stage=="9"and value.process_count):
					self.process_nine=self.process_nine+1
					value.process_count=False
				elif(value.stage=="10" and value.process_count):
					self.process_ten=self.process_ten+1
					value.process_count=False
				elif(value.stage=="11"and value.process_count):
					self.process_eleven=self.process_eleven+1
					value.process_count=False
				elif(value.stage=="12"and value.process_count):
					self.process_twelve=self.process_twelve+1
					value.process_count=False

			
			
	def before_save(self):
		stage_dic = {"1":" 1",
					"2":"2",
					"3":" 3",
					"4":" 4",
					"5":" 5",
					"6":" 6",
					"7":" 7",
					"8":" 8",
					"9":" 9",
					"10":" 10"}
		count = 0
		for i in self.get("required_item") :
			
			if i.stage :
				count += 1
				self.append("item_stage", {
							"item":  i.item ,
							"date": i.date ,
							"current_time":  i.current_time,
							"qty": i.qty,
							"qty_update": i.qty_update,
							"user": i.user,
							"stage": i.stage,
							"actual_used" : i.stage,
							"stages" :stage_dic[str(i.stage)] if str(i.stage) in stage_dic else frappe.throw("Stage not Available")
						})
			else :
				data = self.status + 1
				self.append("item_stage", {
							"item":  i.item ,
							"date": i.date ,
							"current_time":  i.current_time,
							"qty": i.qty,
							"qty_update": i.qty_update,
							"user": i.user,
							"stage": i.stage,
							"actual_used" : data,
							"stages" :stage_dic[str(data)] if str(data) in stage_dic else frappe.throw("Stage not Available")

						})
		if count == 0:
			self.status = self.status + 1
	@frappe.whitelist()
	def get_data(self) :
		d = frappe.get_all('BOM Item',filters = {"parent":self.finished_item},fields=["item_code","stage","qty"])
		
		for i in d :
			if(self.stage==i.stage):
				self.append(
									"item_as_per_bom",
									{
										"item":i.item_code,
										"stage":i.stage,
										"qty":i.qty
						
									}
							)
		frappe.utils.nowdate()
		# a = frappe.get_all('BOM',filters = {"qr_code_data":self.qr_code_data})
		# self.finished_item = a[0]["name"]
		a = frappe.get_all('BOM',filters = {"qr_code_data":self.qr_code_data},fields = ["name","stage"])
		# frappe.throw(str(a))
  
		for data in a :
			# frappe.db.set_value("Required Item For Finished Goods",data.name,"actual_stage",data.stage)
			self.finished_item =data.name
			self.actual_stage =data.stage
			if(self.actual_stage < self.stage):
				frappe.throw(str("Stage Out Of Range"))
      
	

