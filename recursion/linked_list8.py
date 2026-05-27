# linked_list8.py : Program to reverse a single linked list.

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

	def _reverse(self, p):
		if p.link is None:
			return p

		temp = self._reverse(p.link)
		p.link.link = p
		p.link = None

		return temp

	def reverse(self):
		if not self.is_empty():
			self.start = self._reverse(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	lst.reverse()

	print("After reverse, list items are :")
	lst.display()
