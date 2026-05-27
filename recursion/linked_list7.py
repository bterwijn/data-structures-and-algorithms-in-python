# linked_list7.py : Program to delete the last node of a single linked list.

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

	def _del_at_end(self,p):
		if p.link is None:
			return None

		p.link = self._del_at_end(p.link)
		return p

	def del_at_end(self):
		if not self.is_empty():	
			self.start = self._del_at_end(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	lst.del_at_end()

	print("After Deletion of last node, list items are :")
	lst.display()
