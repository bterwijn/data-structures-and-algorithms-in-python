# single_linked_listh.py : Program of single linked list with header node.

class Node:

	def __init__(self,value):
		self.info = value 
		self.link = None 

class SingleLinkedListH:

	def __init__(self, list=None):
		if list == None:
			self.head = Node(0)
		elif list.head.link is None:
			self.head = Node(0)
		else:
			self.head = Node(0)
			p1 = list.head.link
			p2 = self.head.link = Node(p1.info)
			p1 = p1.link

			while p1 is not None:
				p2.link = Node(p1.info)
				p2 = p2.link
				p1 = p1.link
	
	def is_empty(self):
		return (self.head.link == None)

	def display(self):
		if not self.is_empty():
			p = self.head.link
			while p is not None:
				print(p.info)
				p = p.link
		else:
			print("List is empty")

	def insert_at_beginning(self, data):
		temp = Node(data)
		temp.link = self.head.link
		self.head.link = temp
	
	def insert_at_end(self, data):
		temp = Node(data)

		p = self.head
		while p.link is not None:
			p = p.link
		p.link = temp
	
	def insert_before(self, data, node_data):
		p = self.head

		if self.is_empty():
			print("List is empty")
		else:
			# Get p to predecessor of node containing node_data
			while p.link is not None:
				if p.link.info == node_data:
					temp = Node(data)
					temp.link = p.link
					p.link = temp
					break
				p = p.link

			if p.link is None:
				print(f"Item {node_data} is not in the List")

	def insert_after(self, data, node_data):
		p = self.head.link
		if self.is_empty():
			print("List is empty")
		else:
			while p is not None:
				if p.info == node_data:
					temp = Node(data)
					temp.link = p.link
					p.link = temp
					break
				p = p.link

			if p is None:
				print("Item {node_data} is not in the list")
	
	def insert_at_position(self, data, position):
		if position == 1:
			temp = Node(data)
			temp.link = self.head.link
			self.head.link = temp
		else:
			p = self.head.link
			index = 1
			# Get p to (position-1)th node
			while p is not None and index < position-1:
				p = p.link
				index = index+1

			if p is not None and position>0:
				temp = Node(data)
				temp.link = p.link
				p.link = temp
			else:
				print(f"Item cannot be inserted at position : {position}")
	
	def delete_at_beginning(self):
		if self.is_empty():
			print("List is empty")
		else:
			self.head.link = self.head.link.link
	
	def delete_at_end(self):
		p = self.head

		if self.is_empty():
			print("List is empty")
		else:
			while p.link.link is not None:
				p = p.link

			p.link = None
	
	def delete_node(self, node_data):
		p = self.head
		if self.is_empty():
			print("List is empty")
		else:
			while p.link is not None:
				if p.link.info == node_data:
					break
				p = p.link

			if p.link is None:
				print(f"{node_data} not found in list")
			else:
				p.link = p.link.link

	
	def delete_at_position(self, position):
		p = self.head.link

		if self.is_empty():
			print("List is empty")
		elif position == 1:
			self.head.link = p.link
		else:
			index = 1

			while p.link is not None and index < position-1:
				p = p.link
				index = index+1

			if p.link is not None and position>0:
				p.link = p.link.link
			else:
				print(f"Node cannot be deleted at position : {position}")

	def reverse(self):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.head.link
			prev = None

			while p is not None:
				next = p.link
				p.link = prev
				prev = p
				p = next
			self.head.link = prev

if __name__ == '__main__':
	list1 = SingleLinkedListH()

	# Create the List
	list1.insert_at_beginning(10)
	list1.insert_at_end(30)
	list1.insert_after(50,30)
	list1.insert_at_position(20,2)
	list1.insert_before(40,50)

	print("List1 Items after insertion :")
	list1.display()

	list2 = SingleLinkedListH(list1)
	print("List2 Items after using copy constructor :")
	list2.display()

	list1.delete_at_beginning()
	list1.delete_at_end()
	list1.delete_node(30)
	list1.delete_at_position(2)

	print("List1 Items after deletion :")
	list1.display()

	list2.reverse()
	print("List2 Items after reverse :")
	list2.display()
