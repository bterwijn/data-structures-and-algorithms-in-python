# address_calculation_sort.py : Program of sorting using address calculation sort.

class Node:
	def __init__(self,value):
		self.info = value 
		self.link = None

class SortedLinkedList:
	def __init__(self):
			self.start = None
	
	def get_start(self):
		return self.start
	
	def is_empty(self):
		return self.start == None
	
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

def hash_fn(x, large):
	temp = x // large;
	return temp * 5

def address_calculation_sort(lst, n):
	head_list = [SortedLinkedList() for i in range(6)]

	large = 0
	for i in range(n):
		if lst[i] > large:
			large = lst[i]

	for i in range(n):
		x = hash_fn(lst[i],large)
		head_list[x].insert(lst[i])

	# Elements of linked lists are copied to list
	i = 0
	for j in range(6):
		p = head_list[j].get_start()
		while p is not None:
			lst[i] = p.info
			i += 1
			p = p.link

if __name__ == '__main__':
	data_list = [194, 289, 566, 432, 654, 98, 232, 415, 345, 276, 532, 254, 165, 965, 476]

	print("Unsorted list is :")
	print(data_list)

	address_calculation_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
