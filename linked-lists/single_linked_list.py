# single_linked_list.py : Program of Single linked list.

class Node:

	def __init__(self,value):
		self.info = value 
		self.link = None 

class SingleLinkedList:

	def __init__(self, lst=None):
		if lst == None:
			self.start = None
		elif lst.start is None:
			self.start = None
		else:
			p1 = lst.start
			self.start = p2 = Node(p1.info)
			p1 = p1.link

			while p1 is not None:
				p2.link = Node(p1.info)
				p2 = p2.link
				p1 = p1.link

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

	def size(self):
		count = 0
		p = self.start
		while p is not None:
			count = count + 1
			p = p.link
		return count
	
	def find(self, node_data):
		p = self.start
		position = 0

		while p is not None:
			position = position + 1
			if p.info == node_data:
				return position
			p = p.link

		return 0

	def insert_at_beginning(self, data):
		temp = Node(data)
		if not self.is_empty():
			temp.link = self.start
			
		self.start = temp

	def insert_at_end(self, data):
		temp = Node(data)
		if self.is_empty():
			self.start = temp
		else:
			p = self.start
			while p.link is not None:
				p = p.link
			p.link = temp
          
	def insert_after(self, data, node_data):
		p = self.start
		
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
				print(f"Item {node_data} is not in the list")

	def insert_before(self, data, node_data):
		p = self.start

		if self.is_empty():
			print("List is empty") 
		elif p.info == node_data:	# node_data is in first node
			temp = Node(data)
			temp.link = p 
			self.start = temp
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

	def insert_at_position(self, data, position):

		if position == 1:
			temp = Node(data)
			temp.link = self.start
			self.start = temp
		else:
			p = self.start
			index = 1
			# Get p to (position-1)th node
			while p is not None and index < position-1:
				p = p.link
				index = index + 1

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
			self.start = self.start.link
				
	def delete_at_end(self):
		p = self.start

		if self.is_empty():
			print("List is empty")
		elif p.link == None:
			self.start = p.link
		else:
			while p.link.link is not None:
				p = p.link
			p.link = None

	def delete_node(self, node_data):
		p = self.start
		if self.is_empty():
			print("List is empty")
		elif p.info == node_data: # Deletion of first node
			self.start = p.link
		else: # Deletion in between or at the end
			while p.link is not None:
				if p.link.info == node_data:
					break
				p = p.link

			if p.link is None:
				print(f"{nodeData} not found in list")
			else:
				p.link = p.link.link

	def delete_at_position(self, position):
		p = self.start

		if self.is_empty():
			print("List is empty")
		elif(position == 1):
			self.start = self.start.link
		else:
			index = 1

			while p.link is not None and index < position-1:
				p = p.link
				index = index + 1

			if(p.link is not None and position>0):
				p.link = p.link.link
			else:
				print(f"Node cannot be deleted at position : {position}")
                 
	def reverse(self):
		if self.is_empty():
			print("List is empty")
		else:
			p = self.start
			prev = None

			while p is not None:
				next = p.link
				p.link = prev
				prev = p
				p = next

			self.start = prev

	def selection_sort_exchange_data(self):
		p = self.start

		while p.link is not None:
			q=p.link
			while q is not None:
				if p.info > q.info:
					p.info,q.info = q.info,p.info
				q=q.link
			p=p.link

	def selection_sort_exchange_links(self):
		r = p = self.start
		
		while p.link is not None:
			s = q = p.link
			while q is not None:
				if p.info > q.info:
					p.link,q.link = q.link,p.link
					
					if p is not self.start:
						r.link = q
					
					s.link = p
					if p == self.start:
						self.start = q
					
					p,q = q,p
				s = q
				q = q.link
			r = p
			p = p.link

	def bubble_sort_exchange_data(self):
		q = None

		end = None
		while end != self.start.link:
			p = self.start
			while p.link != end:
				q = p.link
				if p.info > q.info:
					p.info,q.info = q.info,p.info
				p = p.link
			end = q

	def bubble_sort_exchange_links(self):
		end = None
		while end != self.start.link:
			r = p = self.start
			while p.link != end:
				q = p.link
				if p.info > q.info:
					p.link = q.link
					q.link = p
					if p != self.start:
						r.link = q
					else:
						self.start = q

					# Rearranging the position of p and q for next pass
					p,q = q,p
				r = p
				p = p.link
			end = q
			
	def merge_lists1(self, lst, merged_list):
		merged_list.start = self._merge1(self.start, lst.start)

	# Merging 2 lists to another new list
	def _merge1(self, p1, p2):
		if p1.info <= p2.info:
			start_m = Node(p1.info)
			p1 = p1.link
		else:
			start_m = Node(p2.info)
			p2 = p2.link

		pm = start_m

		while p1 is not None and p2 is not None:
			if p1.info <= p2.info:
				pm.link = Node(p1.info)
				p1 = p1.link
			else:
				pm.link = Node(p2.info)
				p2 = p2.link
			pm = pm.link

		# Second list is finished. Add the elements of first list.
		while p1 is not None:
			pm.link = Node(p1.info)
			p1 = p1.link
			pm = pm.link

		# First list is finished. Add the elements of second list.
		while p2 is not None:
			pm.link = Node(p2.info)
			p2 = p2.link
			pm = pm.link

		return start_m

	def merge_lists2(self, lst, merged_list):
		merged_list.start = self._merge2(self.start, lst.start)
		self.start = None
		lst.start = None

	# Merging lists by exchanging links
	def _merge2(self, p1, p2):
		if p1.info <= p2.info:
			start_m = p1
			p1 = p1.link
		else:
			start_m = p2
			p2 = p2.link

		pm = start_m

		while p1 is not None and p2 is not None:
			if p1.info <= p2.info:
				pm.link = p1
				p1 = p1.link
				pm = pm.link
			else:
				pm.link = p2
				p2 = p2.link
				pm = pm.link

		# Second list is finished. Add the remaining elements of first list
		if p1 is not None:
			pm.link = p1

		# First list is finished. Add the remaining elements of second list
		if p2 is not None:
			pm.link = p2

		return start_m

	def merge_lists2(self, lst, merged_list):
		merged_list.start = self._merge2(self.start, lst.start)
		self.start = None
		lst.start = None

	# Merging lists by exchanging links
	def _merge2(self, p1, p2):
		if p1.info <= p2.info:
			start_m = p1
			p1 = p1.link
		else:
			start_m = p2
			p2 = p2.link

		pm = start_m

		while p1 is not None and p2 is not None:
			if p1.info <= p2.info:
				pm.link = p1
				p1 = p1.link
				pm = pm.link
			else:
				pm.link = p2
				p2 = p2.link
				pm = pm.link

		# Second list is finished. Add the remaining elements of first list
		if p1 is not None:
			pm.link = p1

		# First list is finished. Add the remaining elements of second list
		if p2 is not None:
			pm.link = p2

		return start_m
		
	def merge_sort(self):
		self.start = self._merge_sort_rec(self.start)

	def _merge_sort_rec(self, list_start):
		# If the list is empty or has only one node
		if list_start is None or list_start.link is None:
			return list_start

		# If more than one element
		start1 = list_start
		start2 = self._divide_list(list_start)
		start1 = self._merge_sort_rec(start1)
		start2 = self._merge_sort_rec(start2)
		start_m = self._merge2(start1, start2)

		return start_m

	def _divide_list(self, p):
		q = p.link.link

		while q is not None and q.link is not None:
			p = p.link
			q = q.link.link

		start2 = p.link
		p.link = None

		return start2

	def concatenate(self, lst):
		if self.start is None:
			self.start = lst.start
			return

		if lst.start is None:   
			return

		p = self.start
		while p.link is not None:
			p = p.link

		p.link = lst.start
		lst.start = None

	def insert_cycle(self, node_data):
		cycle_p = None

		if self.start is None or self.start.link is None:
			print("Cycle cannot be inserted")
		else:
			p = self.start
			prev = self.start
			while p is not None:
				if p.info == node_data:
					cycle_p = p

				prev = p
				p = p.link

			if cycle_p is not None:
				print(f"cycle_p.info : {cycle_p.info}")
				prev.link = cycle_p

				# Display the list
				p = self.start
				while p != cycle_p:
					print(f"p.info = {p.info}")
					p = p.link

				p = cycle_p
				print(f"p.info = {p.info}")
				p = p.link
				while p != cycle_p:
					print(f"p.info = {p.info}")
					p = p.link
			else:
				print(f"{node_data} is not found in the list")
	
	def _find_cycle(self):
		if self.start is None or self.start.link is None:
			return None
		else:
			slow_p = self.start
			fast_p = self.start

			while fast_p is not None and fast_p.link is not None:
				slow_p = slow_p.link
				fast_p = fast_p.link.link

				if slow_p == fast_p:
					print("slow_p and fast_p meets here")
					print(f"slow_p.info = {slow_p.info}")
					print(f"fast_p.info = {fast_p.info}")

					return slow_p

			return None

	def has_cycle(self):
		if self._find_cycle() is not None:
			return True
		else:
			return False

	def remove_cycle(self):
		p = self._find_cycle()

		if p is None:
			print("There is no cycle in list.")
		else:
			print(f"Node where cycle was detected : {p.info}")
			p1 = p
			p2 = p

			# Find the length of cycle
			cycle_length = 0
			cycle_length = cycle_length + 1
			p1 = p1.link
			while p1 != p2:
				cycle_length = cycle_length + 1
				p1 = p1.link

			print(f"Cycle Length : {cycle_length}")

			# Find the remaining length
			rem_length = 0
			p1 = self.start
			while p1 != p2:
				rem_length = rem_length + 1
				p1 = p1.link
				p2 = p2.link

			print(f"Remaining Length : {rem_length}")

			list_length = cycle_length + rem_length

			print("The List is :")
			p1 = self.start
			
			i = 1
			while i <= list_length-1:
				print(p1.info)
				p1 = p1.link
				i = i + 1
			
			print(p1.info)
			p1.link = None

if __name__ == '__main__':
	list1 = SingleLinkedList()

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

	list2 = SingleLinkedList(list1)
	print("List2 Items after copy :")
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

	list3 = SingleLinkedList()
	list3.insert_at_end(20)
	list3.insert_at_end(10)
	list3.insert_at_end(50)
	list3.insert_at_end(30)
	list3.insert_at_end(40)

	print("List3 Items :")
	list3.display()		

	list4 = SingleLinkedList(list3) 
	list4.selection_sort_exchange_data()
	print("List4 Items after selection sort (exchange data) :")
	list4.display()

	list5 = SingleLinkedList(list3) 
	list5.selection_sort_exchange_links()
	print("List5 Items after selection sort (exchange links) :")
	list5.display()

	list6 = SingleLinkedList(list3) 
	list6.bubble_sort_exchange_data()
	print("List6 Items after bubble sort (exchange data) :")
	list6.display()

	list7 = SingleLinkedList(list3)
	list7.bubble_sort_exchange_links()
	print("List7 Items after bubble sort (exchange links) :")
	list7.display()

	list8 = SingleLinkedList()
	list9 = SingleLinkedList()
	list10 = SingleLinkedList()
	list11 = SingleLinkedList()

	list8.insert_at_end(10)
	list8.insert_at_end(20)
	list8.insert_at_end(30)
	list8.insert_at_end(40)
	list8.insert_at_end(50)

	print("List8 Items :")
	list8.display()

	list9.insert_at_end(15)
	list9.insert_at_end(25)
	list9.insert_at_end(30)
	list9.insert_at_end(45)
	list9.insert_at_end(55)

	print("List9 Items :")
	list9.display()

	list8.merge_lists1(list9, list10)
	print("List10 Items - Mergeing 2 Lists to another new list :")
	list10.display()

	list8.merge_lists2(list9, list11)
	print("List11 Items - Merged List (exchange links) :")
	list11.display()

	list12 = SingleLinkedList()

	list12.insert_at_end(10)
	list12.insert_at_end(5)
	list12.insert_at_end(20)
	list12.insert_at_end(15)
	list12.insert_at_end(30)
	list12.insert_at_end(25)
	list12.insert_at_end(40)
	list12.insert_at_end(35)

	print("List12 Items :")
	list12.display()

	list12.merge_sort()

	print("List12 Items after merge sort :")
	list12.display()

	list13 = SingleLinkedList()
	list14 = SingleLinkedList()

	list13.insert_at_end(10)
	list13.insert_at_end(20)
	list13.insert_at_end(30)
	list13.insert_at_end(40)
	list13.insert_at_end(50)

	print("List13 Items :")
	list13.display()

	list14.insert_at_end(5)
	list14.insert_at_end(15)
	list14.insert_at_end(25)
	list14.insert_at_end(35)
	list14.insert_at_end(45)

	print("List14 Items :")
	list14.display()

	list13.concatenate(list14)

	print("List13 Items after concatenation :")
	list13.display()

	list15 = SingleLinkedList()

	list15.insert_at_end(10)
	list15.insert_at_end(20)
	list15.insert_at_end(30)
	list15.insert_at_end(40)
	list15.insert_at_end(50)
	list15.insert_at_end(60)
	list15.insert_at_end(70)
	list15.insert_at_end(80)

	print("Finding a cycle and its removal in list :")
	print(f"find(40) = {list15.find(40)}")
	list15.insert_cycle(40)
	print(f"Has cycle : {list15.has_cycle()}")
	list15.remove_cycle()
	print(f"Has cycle : {list15.has_cycle()}")
