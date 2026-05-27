# linked_list1.py : Program to get the length of a single linked list.

class Node:
	def __init__(self,value):
		self.info = value 
		self.link = None 

class SingleLinkedList:
	def __init__(self):
		self.start = None

	def is_empty(self):
		return (self.start == None)	
	
	def insert_at_beginning(self, data):
		temp = Node(data)
		if not self.is_empty():
			temp.link = self.start	
			
		self.start = temp

	def display(self):
		if not self.is_empty():
			p = self.start 
			while p is not None:
				print(p.info)
				p = p.link 
		else:			
			print("List is empty")	

	def _length(self,p):
		if p is None:
			return 0

		return (1 + self._length(p.link))

	def length(self):
		return self._length(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	print(f"Length of list is : {lst.length()}")
