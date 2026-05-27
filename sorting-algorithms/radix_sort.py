# radix_sort.py : Program of sorting using radix sort.

class Node:

	def __init__(self,value):
		self.info = value 
		self.link = None 

# Returns kth digit from right in n
def get_digit(n, k):
	digit = 0
	
	i = 1
	while i<=k:
		digit = n%10
		n //= 10
		i += 1
	
	return digit
	
# Returns number of digits in the largest element of the list
def digits_in_largest(start):
	# Find largest element
	p = start
	large = 0

	while p is not None:
		if p.info > large:
			large = p.info
		p = p.link
	
	# Find number of digits in largest element
	ndigits = 0
	while large != 0:
		ndigits += 1
		large //= 10

	return ndigits

def radix_sort(lst, n):
	start = None

	# Creating linked list by insertion at beginning from lst[n-1]...lst[0]
	i = n-1
	while i >= 0:
		temp = Node(lst[i])
		temp.link = start
		start = temp
		i -= 1

	rear = [None] * 10
	front = [None] * 10
	
	least_sig_pos = 1
	most_sig_pos = digits_in_largest(start)

	k = least_sig_pos
	while k <= most_sig_pos:
		# Make all the queues empty at the beginning of each pass
		for i in range(10):
			rear[i] = None
			front[i] = None
		
		p = start
		while p is not None:
			# Find kth digit from right in the number
			digit = get_digit(p.info, k)
		
			# Insert the node in Queue(digit)
			if front[digit] is None:
				front[digit] = p
			else:
				rear[digit].link = p
			rear[digit] = p
			p = p.link
		
		# Join all the queues to form the new linked list
		i=0
		while front[i] is None: # Finding first non empty queue
			i += 1

		start = front[i]
		while i <= 8: 
			if rear[i+1] is not None: #if (i+1)th  queue is not empty
				rear[i].link = front[i+1] # join end of ith queue to start of (i+1)th queue
			else:
				rear[i+1] = rear[i]		# continue with rear[i]
			i += 1

		rear[9].link = None

		k += 1

	# Copying linked list to lst and deleting the linked list
	i=0
	p=start
	while p is not None:
		lst[i] = p.info
		i += 1
		p = p.link
		start = None
		start = p

if __name__ == '__main__':
	data_list = [62, 234, 456, 750, 789, 3, 21, 345, 983, 99, 153, 65, 23, 5, 98, 10, 6, 372]

	print("Unsorted list is :")
	print(data_list)

	radix_sort(data_list, len(data_list))

	print("Sorted list is :")
	print(data_list)
