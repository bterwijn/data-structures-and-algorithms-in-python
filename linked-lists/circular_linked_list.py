# circular_linked_list.py : Program of Circular linked list.

class Node:

	def __init__(self,value):
		self.info = value 
		self.link = None 

class CircularLinkedList:
	def __init__(self, list=None):
		if list == None:
			self.last = None
		elif list.last is None:
			self.last = None
		else:
			p1 = list.last.link
			p2 = self.last = Node(p1.info)
			self.last.link = self.last
			p1 = p1.link

			while p1 is not list.last.link:
				temp = Node(p1.info)
				temp.link = p2.link
				p2.link = temp
				p2 = p2.link
				self.last = p2
				p1 = p1.link
	
	def is_empty(self):
		return (self.last == None)

	def display(self):
		if not self.is_empty():
			p = self.last.link
			print(p.info)
			p = p.link
			while p != self.last.link:
				print(p.info)
				p = p.link
		else:
			print("List is empty")

	def insert_at_beginning(self, data):
		temp = Node(data)
		if self.is_empty():
			self.last = temp
			self.last.link = temp
		else:
			temp.link = self.last.link
			self.last.link = temp
	
	def insert_at_end(self, data):
		temp = Node(data)

		if self.is_empty():
			self.last = temp
			self.last.link = temp
		else:
			temp.link = self.last.link
			self.last.link = temp
			self.last = temp

	def insert_before(self, data, node_data):
		p = self.last

		if self.is_empty():
			print("List is empty")
		elif p.link.info == node_data: # nodeData is in first node
			temp = Node(data)
			temp.link = p.link
			p.link = temp
		else:
			p = self.last.link
			if p.link.info == node_data:
				temp = Node(data)
				temp.link = p.link
				p.link = temp
				return
			p = p.link
			
			while p is not self.last.link:
				if p.link.info == node_data:
					temp = Node(data)
					temp.link = p.link
					p.link = temp
					break
				p = p.link

			if p == self.last.link:
				print(f"Item {node_data} is not in the list")

	def insert_after(self, data, node_data):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.last.link

			if p.info == node_data:
				temp = Node(data)
				temp.link = p.link
				p.link = temp
				if p is self.last:
					self.last = temp
				return
			p = p.link
			
			while p is not self.last.link:
				if p.info == node_data:
					temp = Node(data)
					temp.link = p.link
					p.link = temp
					if p is self.last:
						self.last = temp
					break
				p = p.link

			if p is self.last.link:
				print(f"Item {node_data} is not in the list")

	def insert_at_position(self, data, position):
		p = self.last

		if self.is_empty():
			if position == 1:
				temp = Node(data)
				self.last = temp
				self.last.link = temp
			else:
				print(f"Item cannot be inserted at position : {position}")
		elif position == 1:
			temp = Node(data)
			temp.link = self.last.link
			self.last.link = temp
		else:
			p = self.last.link
			index = 1
			
			if index == position-1:
				temp = Node(data)
				temp.link = p.link
				p.link = temp
				if p == self.last:
					self.last = temp
				p = p.link
				return
			index = index + 1
			p = p.link			
			
			while p is not self.last.link:
				if index == position-1:
					temp = Node(data)
					temp.link = p.link
					p.link = temp
					if p == self.last:
						self.last = temp
					p = p.link
					break
				index = index + 1
				p = p.link

			if p == self.last.link:
				print(f"Item cannot be inserted at position : {position}")

	def delete_at_beginning(self):
		if self.is_empty():
			print("List is empty")
		elif self.last.link == self.last: # List has only one node
			self.last = None
		else:
			self.last.link = self.last.link.link

	def delete_at_end(self):
		if self.is_empty():
			print("List is empty")
		elif self.last.link == self.last: # List has only one node
			self.last = None
		else:
			p = self.last.link
			while p.link is not self.last:
				p = p.link

			p.link = self.last.link
			self.last = p

	def delete_node(self, node_data):
		if self.is_empty():
			print("List is empty")
		elif self.last.link.info == node_data: # Deletion of first node
			if self.last.link == self.last: # List has only one node
				self.last = None
			else:
				self.last.link = self.last.link.link
		else: # Deletion in between or at the end
			p = self.last.link

			while p.link != self.last.link:
				if p.link.info == node_data:
					break
				p = p.link

			if p.link == self.last.link:
				print(f"{node_data} not found in list")
			else:
				if p.link == self.last:
					self.last = p
				p.link = p.link.link

	def delete_at_position(self, position):
		if self.is_empty():
			print("List is empty")
		elif position == 1: # Deletion of first node
			if self.last.link == self.last: # List has only one node
				self.last = None
			else:
				self.last.link = self.last.link.link
		else: # Deletion in between or at the end
			p = self.last.link
			index = 1

			while p.link != self.last.link:
				if index == position-1:
					break
				index = index+1
				p = p.link

			if p.link == self.last.link:
				print(f"Node cannot be deleted at position : {position}")
			else:
				if p.link == self.last:
					self.last = p
				p.link = p.link.link

	def reverse(self):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.last.link
			prev = self.last

			while p.link != self.last.link:
				next = p.link
				p.link = prev
				prev = p
				p = next
			self.last = p.link
			self.last.link = p
			p.link = prev

	def concatenate(self, list):
		if self.last is None:
			self.last = list.last
			list.last = None
		elif list.last is not None:
			p = self.last.link
			self.last.link = list.last.link
			list.last.link = p
			self.last = list.last
			list.last = None

if __name__ == '__main__':
	list1 = CircularLinkedList()

	# Create the List
	list1.insert_at_beginning(10)
	list1.insert_at_end(30)
	list1.insert_after(50,30)
	list1.insert_at_position(20,2)
	list1.insert_before(40,50)

	print("List1 Items after insertion :")
	list1.display()

	list2 = CircularLinkedList(list1)
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

	list4 = CircularLinkedList()
	list5 = CircularLinkedList()

	list4.insert_at_end(10)
	list4.insert_at_end(20)
	list4.insert_at_end(30)
	list4.insert_at_end(40)
	list4.insert_at_end(50)

	print("List4 Items :")
	list4.display()

	list5.insert_at_end(5)
	list5.insert_at_end(15)
	list5.insert_at_end(25)
	list5.insert_at_end(35)
	list5.insert_at_end(45)

	print("List5 Items :")
	list5.display()

	list4.concatenate(list5)

	print("List4 Items after concatenation :")
	list4.display()
