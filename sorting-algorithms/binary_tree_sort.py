# binary_tree_sort.py : Program of sorting using binary tree sort.

class Node:
	def __init__(self,value):
		self.info = value 
		self.lchild = None
		self.rchild = None

class BinarySearchTree:
	def __init__(self):
		self._root = None
		self._k = 0

	def is_empty(self):
		return _root == None
	
	def _insert(self, p, data):
		if p is None:
			p = Node(data)
		elif data < p.info:
			p.lchild = self._insert(p.lchild, data)
		else:
			p.rchild = self._insert(p.rchild, data)
		return p
	
	def insert(self, data):
		self._root = self._insert(self._root, data)
	
	# Recursive inorder traversal
	def _inorder(self, p, lst):
		if p is None:
			return
		self._inorder(p.lchild,lst)
		lst[self._k] = p.info
		self._k += 1
		self._inorder(p.rchild,lst)
	
	def inorder(self, lst):
		self._k = 0
		self._inorder(self._root,lst)

def binary_tree_sort(lst, n):
	bst = BinarySearchTree()

	for i in range(n):
		bst.insert(lst[i])
	bst.inorder(lst)

if __name__ == '__main__':
	data_list = [19, 35, 10, 12, 46, 6, 40, 3, 90, 8]

	print("Unsorted list is :")
	print(data_list)

	binary_tree_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
