# heap_tree.py : Program for Heap Tree.

class HeapTree:
	def __init__(self, max_size=30):
		self.heap_list = [None] * max_size # list for heap
		self.n = 0		# Number of elements in heap
		self.heap_list[0] = 9999

	def is_empty(self):
		return self.n==0

	def insert(self, key):
		self.n += 1	# Increase the heap size by 1
		self.heap_list[self.n] = key
		self._restore_up(self.n)

	def _restore_up(self, i):
		k = self.heap_list[i]
		i_parent = i//2

		while self.heap_list[i_parent] < k:
			self.heap_list[i] = self.heap_list[i_parent]
			i = i_parent
			i_parent = i//2

		self.heap_list[i] = k
	
	def delete_heap(self):
		if self.is_empty():
			raise Exception("Tree is empty.")

		max_value = self.heap_list[1]	# Save the element present at the root
		self.heap_list[1] = self.heap_list[self.n]	# Place the last element in the root
		self.n -= 1						# Decrease the heap size by 1
		self._restore_down(1)

		return max_value
	
	def _restore_down(self, i):
		k = self.heap_list[i]
		lchild = 2*i
		rchild = lchild+1

		while rchild <= self.n:
			if self.heap_list[lchild]<=k and self.heap_list[rchild]<=k:
				self.heap_list[i] = k
				return
			elif self.heap_list[lchild] > self.heap_list[rchild]:
				self.heap_list[i] = self.heap_list[lchild]
				i = lchild
			else:
				self.heap_list[i] = self.heap_list[rchild]
				i = rchild

			lchild = 2*i
			rchild = lchild+1

		# If number of nodes is even
		if lchild==self.n and k<self.heap_list[lchild]:
			self.heap_list[i] = self.heap_list[lchild]
			i = lchild

		self.heap_list[i] = k
	
	def display(self):
		i = 1
		while i <= self.n:
			print(f"{self.heap_list[i]} ", end='')
			i += 1
		print()
		print(f"Number of elements = {self.n}")

if __name__ == '__main__':
	heap_tree = HeapTree(30);

	try:
		heap_tree.insert(25)
		heap_tree.display()
		heap_tree.insert(35)
		heap_tree.display()
		heap_tree.insert(18)
		heap_tree.display()
		heap_tree.insert(9)
		heap_tree.display()
		heap_tree.insert(46)
		heap_tree.display()
		heap_tree.insert(70)
		heap_tree.display()
		heap_tree.insert(48)
		heap_tree.display()
		heap_tree.insert(23)
		heap_tree.display()
		heap_tree.insert(78)
		heap_tree.display()
		heap_tree.insert(12)
		heap_tree.display()
		heap_tree.insert(95)

		print("After Insertion :")
		heap_tree.display()

		print("After Deletion :")
		print(f"Maximum Element : {heap_tree.delete_heap()}")
		heap_tree.display()
		print(f"Maximum Element : {heap_tree.delete_heap()}")
		heap_tree.display()
	except Exception as e:
		print(e)
