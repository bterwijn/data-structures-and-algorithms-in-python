# sorted_linked_list.py : Program of sorted linked list.

class Node:

	def __init__(self,value):
		self.info = value 
		self.link = None 

class SortedLinkedList:

	def __init__(self):
			self.start = None

	def is_empty(self):
		return (self.start == None)

	def display(self):
		if not self.is_empty():
			p = self.start 
			while p is not None:
				print(p.info)
				p = p.link 
		else:			
			print("List is empty")

	def find(self, node_data):
		p = self.start
		position = 0

		while p is not None:
			position = position + 1
			if p.info == node_data:
				return position
			p = p.link

		return 0

	def insert(self, data):
		temp = Node(data)
		
		# List empty or new node to be inserted before first node
		if self.is_empty() or data < self.start.info:
			temp.link = self.start
			self.start = temp	
		else:
			p = self.start
			while p.link is not None and p.link.info < data:
				p = p.link
			temp.link = p.link
			p.link = temp

if __name__ == '__main__':
	list = SortedLinkedList()

	list.insert(10)
	list.insert(20)
	list.insert(15)
	list.insert(40)
	list.insert(50)

	print("List Items :")
	list.display()

	print(f"find(40) = {list.find(40)}")
