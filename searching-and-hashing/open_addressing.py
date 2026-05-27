# open_addressing.py : Program of Open Addressing - Linear Probing

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
	
class HashTable:
	def __init__(self, size=11):
		self.m = size	# size of list
		self.n = 0		# number of employee records
		self.emp_list = [None] * self.m
		self.status = [None] * self.m
		self.EMPTY = 0
		self.DELETED = 1
		self.OCCUPIED = 2

		for i in range(0,self.m):
			self.status[i] = self.EMPTY

	def _hash(self, key):
		return key%self.m

	def insert(self, emp):
		key = emp.get_employee_id()
		h = self._hash(key)

		location = h

		for i in range(1,self.m):
			if self.status[location]==self.EMPTY or self.status[location]==self.DELETED:
				self.emp_list[location] = emp
				self.status[location] = self.OCCUPIED
				self.n += 1
				return

			if self.emp_list[location].get_employee_id() == key:
				print("Duplicate key")
				return

			location = (h+i)%self.m
		
		print("Table is full")
	
	def search(self, key):
		h = self._hash(key)
		location = h

		for i in range(1,self.m):
			if self.status[location]==self.EMPTY or self.status[location]==self.DELETED:
				return False

			if self.emp_list[location].get_employee_id() == key:
				print(self.emp_list[location])
				return True

			location = (h+i)%self.m

		return False
	
	def del_key(self, key):
		h = self._hash(key)
		location = h

		for i in range(1,self.m):
			if self.status[location]==self.EMPTY or self.status[location]==self.DELETED:
				print("Key not found")
				return

			if self.emp_list[location].get_employee_id() == key:
				self.status[location] = self.DELETED
				self.n -= 1
				print(f"Record {self.emp_list[location]} deleted")
				return

			location = (h+i)%self.m
	
	def display(self):
		for i in range(self.m):
			print(f"[{i}] --> ", end='')

			if self.status[i] == self.OCCUPIED:
				print(self.emp_list[i])
			else:
				print("___")

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
