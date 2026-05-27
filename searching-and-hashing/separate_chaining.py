# separate_chaining.py : Program of Separate Chaining.

class Employee:
	def __init__(self, id, name):
		self.employee_id = id
		self.employee_name = name

	def get_employee_id(self):
		return self.employee_id

	def set_employee_id(self, id):
		self.employee_id = id
	
	def __str__(self):
		return str(self.employee_id) + " "  + self.employee_name

class Node:
	def __init__(self, data):
		self.info = data
		self.link = None

class SingleLinkedList:
	def __init__(self):
		self.start = None

	def is_empty(self):
		return self.start==None
	
	def display(self):
		if not self.is_empty():
			p = self.start
			while p is not None:
				print(f"{p.info} ",end='')
				p = p.link
			print()
		else:
			print(" ___")
	
	def search(self, key):
		p = self.start
		
		while p is not None:
			if p.info.get_employee_id() == key:
				break
			p = p.link

		return p
	
	def insert_at_beginning(self, data):
		temp = Node(data)
		if not self.is_empty():
			temp.link = self.start

		self.start = temp
	
	def delete_node(self, key):
		p = self.start
		if self.is_empty():
			print(f"Key {key} not present")
		elif p.info.get_employee_id() == key: # Deletion of first node
			self.start = p.link
		else:	# Deletion in between or at the end
			while p.link is not None:
				if p.link.info.get_employee_id() == key:
					break
				p = p.link

			if p.link is None:
				print(f"Key {key} not present")
			else:
				p.link = p.link.link

class HashTable:
	def __init__(self, size=11):
		self.m = size	# size of the list
		self.n = 0		# number of records
		self.emp_list = [None] * self.m
	
	def _hash(self, key):
		return key%self.m
	
	def search(self, key):
		h = self._hash(key)
		p = self.emp_list[h].search(key)

		if p is not None:
			print(p.info)
			return True

		return False
	
	def insert(self, emp):
		key = emp.get_employee_id()
		h = self._hash(key)
		
		if self.emp_list[h] is None:
			self.emp_list[h] = SingleLinkedList()		
		
		if self.search(key):
			print(" Duplicate key")
			return

		self.emp_list[h].insert_at_beginning(emp)
		self.n += 1
	
	def del_key(self, key):
		h = self._hash(key)
		self.emp_list[h].delete_node(key)
		self.n -= 1
	
	def display(self):
		for i in range(0,self.m):
			print(f"[{i}]  -->",end='')

			if self.emp_list[i] is not None:
				self.emp_list[i].display()
			else:
				print(" ___")

if __name__ == '__main__':
	table = HashTable()

	table.insert(Employee(15,"Suresh"))
	table.insert(Employee(28,"Manish"))
	table.insert(Employee(20,"Abhishek"))
	table.insert(Employee(45,"Srikant"))
	table.insert(Employee(82,"Rajesh"))
	table.insert(Employee(98,"Amit"))
	table.insert(Employee(77,"Vijay"))
	table.insert(Employee(9,"Alok"))
	table.insert(Employee(34,"Vimal"))
	table.insert(Employee(49,"Deepak"))

	table.display()

	print(f"search(15) : {table.search(15)}")

	table.del_key(15)
	print(f"search(15) : {table.search(15)}")

	table.display()
