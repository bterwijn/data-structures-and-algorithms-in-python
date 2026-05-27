# linked_list4.py : Program to display the elements of a single linked list in reverse order.

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

	def _rdisplay(self,p):
		if p is None:
			return

		self._rdisplay(p.link)
		print(p.info)
			
	def rdisplay(self):
		self._rdisplay(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	print("List Items in reverse order :")
	lst.rdisplay()
