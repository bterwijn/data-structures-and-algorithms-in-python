# linked_list5.py : Program to find an element in a single linked list.

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

	def _search(self, p, data):
		if p is None:
			return False

		if p.info == data:
			return True

		return self._search(p.link, data)

	def search(self, data):
		return self._search(self.start, data)

if __name__ == '__main__':
	lst = SingleLinkedList()

	lst.insert_at_beginning(50)
	lst.insert_at_beginning(40)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(20)
	lst.insert_at_beginning(10)

	print("List Items :")
	lst.display()

	node_data = 40

	print(f"List node {node_data} found : {lst.search(node_data)}")
