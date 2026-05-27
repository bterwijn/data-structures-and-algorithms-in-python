# doubly_linked_list.py : Program of Doubly linked list.

class Node:
	def __init__(self,value):
		self.info = value 
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self, lst=None):
		if lst == None:
			self.start = None
		elif lst.start is None:
			self.start = None
		else:
			p1 = lst.start
			p2 = self.start = Node(p1.info)
			previous = None
		
			p1 = p1.next

			while p1 is not None:
				p2.next = Node(p1.info)
				p2.prev = previous
				previous = p2
				p2 = p2.next
				p1 = p1.next
			p2.prev = previous
		
	def is_empty(self):
		return (self.start == None)

	def display(self):
		if not self.is_empty():
			p = self.start 
			while p is not None:
				print(p.info)
				p = p.next 
		else:			
			print("List is empty")

	def size(self):
		count = 0
		p = self.start
		while p is not None:
			count = count + 1
			p = p.next
		return count

	def find(self, node_data):
		p = self.start
		position = 0

		while p is not None:
			position = position + 1
			if p.info == node_data:
				return position
			p = p.next

		return 0

	def insert_at_beginning(self, data):
		temp = Node(data)
		if not self.is_empty():
			temp.next = self.start
			self.start.prev = temp
			
		self.start = temp

	def insert_at_end(self, data):
		temp = Node(data)

		if self.is_empty():
			self.start = temp
		else:
			p = self.start
			while p.next is not None:
				p = p.next

			p.next = temp
			temp.prev = p

	def insert_before(self, data, node_data):
		if self.is_empty():
			print("List is empty")
		elif self.start.info == node_data: # node_data is in first node
			temp = Node(data)
			temp.next = self.start
			self.start.prev = temp
			self.start = temp
		else:
			p = self.start.next
			while p is not None:
				if p.info == node_data:
					temp = Node(data)
					temp.prev = p.prev
					temp.next = p
					p.prev.next = temp
					p.prev = temp
					break
				p = p.next

			if p is None:
				print(f"Item {node_data} is not in the List")
			
	def insert_after(self, data, node_data):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			while p is not None:
				if p.info == node_data:
					temp = Node(data)
					temp.prev = p
					temp.next = p.next
					if p.next is not None:
						p.next.prev = temp # should not be done when p refers to last node
					p.next = temp
					break
				p = p.next

			if p is None:
				print(f"Item {node_data} is not in the list")

	def insert_at_position(self, data, position):
		if position == 1:
			temp = Node(data)
			if not self.is_empty():
				temp.next = self.start
				self.start.prev = temp
			self.start = temp
		else:
			p = self.start
			index = 1
			# Getting p to (position-1)th node
			while p is not None and index < position-1 : 
				p = p.next
				index = index + 1

			if p is not None and position > 0 :
				temp = Node(data)
				temp.prev = p
				temp.next = p.next
				if p.next is not None:
					p.next.prev = temp # should not be done when p refers to last node
				p.next = temp
			else:
				print(f"Item cannot be inserted at position : {position}")

	def delete_at_beginning(self):
		if self.is_empty():
			print("List is empty")
		else:
			if self.start.next is None: # If list has only 1 node
				self.start = None
			else:
				self.start = self.start.next
				self.start.prev = None

	def delete_at_end(self):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			while p.next is not None:
				p = p.next

			if p.prev is not None:
				p.prev.next = None
			else:
				self.start = None
				
	def delete_node(self, node_data):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			while p.next is not None:
				if p.info == node_data:
					break
				p = p.next

			if p.info == node_data:
				if p.next is None:
					if p.prev is None: # First and only node
						self.start = None
					else:
						p.prev.next = None # Last node
				else:
					if p.prev is None: # First node
						p.next.prev = None
						self.start = p.next
					else: # Node in between
						p.prev.next = p.next
						p.next.prev = p.prev
			else:
				print(f"{node_data} not found in list")
	
	def delete_at_position(self, position):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			index = 1
			while p.next is not None:
				if index == position:
					break
				index = index+1
				p = p.next

			if position == 1:
				if p.next is None: # First node of only node in list
					self.start = None
				else: # First node of more than one node in list
					p.next.prev = None
					self.start = p.next
			elif index == position:
				if p.next is None:
					p.prev.next = None
				else:
					p.next.prev = p.prev
					p.prev.next = p.next
			else:
				print(f"Node cannot be deleted at position : {position}")

	def reverse(self):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			while p.next is not None:
				temp = p.next
				p.next = p.prev
				p.prev = temp
				p = temp
			p.next = p.prev
			p.prev = None
			self.start = p
	
if __name__ == '__main__':
	list1 = DoublyLinkedList()

	# Create the List
	list1.insert_at_beginning(10)
	list1.insert_at_end(30)
	list1.insert_after(50,30)
	list1.insert_at_position(20,2)
	list1.insert_before(40,50)

	print("List1 Items after insertion :")
	list1.display()

	print(f"Total items : {list1.size()}")
	print(f"find(40) = {list1.find(40)}")

	list2 = DoublyLinkedList(list1)
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
