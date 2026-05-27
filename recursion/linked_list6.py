# linked_list6.py : Program to insert a node at the end of a single linked list.

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

	def _insert_at_end(self, p, data):
		if p is None:
			temp = Node(data)
			return temp

		p.link = self._insert_at_end(p.link, data)
		return p

	def insert_at_end(self,data):
		self.start = self._insert_at_end(self.start, data)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	data = 75
	lst.insert_at_end(data)

	print(f"After inserting {data} at the end, list items are :")
	lst.display()
