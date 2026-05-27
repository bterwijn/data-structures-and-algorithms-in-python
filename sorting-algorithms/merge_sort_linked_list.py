# merge_sort_linked_list.py : Program of sorting using merge sort on linked list.

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
				print(f"{p.info} ", end='')
				p = p.link
			print()
		else:			
			print("List is empty")
	
	def _merge(self,p1,p2):
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
				pm = pm.link
				p1 = p1.link
			else:
				pm.link = p2
				pm = pm.link
				p2 = p2.link

		if p1 is None:
			pm.link = p2
		else:
			pm.link = p1
	     
		return start_m
	
	def _divide_list(self,p):
		q = p.link.link

		while q is not None and q.link is not None:
			p = p.link
			q = q.link.link

		start2 = p.link
		p.link = None

		return start2
	
	def _merge_sort_rec(self,list_start):
		# if list empty or has one element
		if list_start is None or list_start.link is None:
			return list_start

		# if more than one element
		start1 = list_start
		start2 = self._divide_list(list_start)
		start1 = self._merge_sort_rec(start1)
		start2 = self._merge_sort_rec(start2)
		start_m = self._merge(start1, start2)
		return start_m

	def merge_sort(self):
		self.start = self._merge_sort_rec(self.start)

if __name__ == '__main__':
	lst = SingleLinkedList()

	# Create the List
	lst.insert_at_beginning(3)
	lst.insert_at_beginning(56)
	lst.insert_at_beginning(21)
	lst.insert_at_beginning(4)
	lst.insert_at_beginning(64)
	lst.insert_at_beginning(92)
	lst.insert_at_beginning(42)
	lst.insert_at_beginning(30)
	lst.insert_at_beginning(89)
	lst.insert_at_beginning(5)
	lst.insert_at_beginning(8)

	print("List items :")
	lst.display()

	lst.merge_sort()

	print("List items after merge sort on list :")
	lst.display()
