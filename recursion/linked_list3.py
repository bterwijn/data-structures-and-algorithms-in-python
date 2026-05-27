# linked_list3.py : Program to display the elements of a single linked list.

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

	def _display(self, p):
		if p is None:
			return

		print(p.info)
		self._display(p.link)
	
	def display(self):
		self._display(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()