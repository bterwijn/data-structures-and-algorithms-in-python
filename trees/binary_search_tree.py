# binary_search_tree.py : Program for Binary Search Tree.

class Node:
	def __init__(self,key):
		self.info = key 
		self.lchild = None
		self.rchild = None

class BinarySearchTree:
	def __init__(self, bst=None):
		if bst == None:
			self.root = None
		elif bst.root is None:
			self.root = None
		else:
			self.root = self._copy(bst.root)

	def _copy(self, p):
		if p is None:
			return None

		cp = Node(p.info)
		cp.lchild = self._copy(p.lchild)
		cp.rchild = self._copy(p.rchild)
		return cp
	
	def is_empty(self):
		return self.root==None
	
	# Non Recursive insertion
	def insert1(self, key):
		parent = None
		p = self.root

		while p is not None:
			parent = p

			if key < p.info:
				p = p.lchild
			elif key > p.info:
				p = p.rchild
			else:
				print(f"{key} is already there")
				return

		temp = Node(key)

		if parent is None:
			self.root = temp
		elif key < parent.info:
			parent.lchild = temp
		else:
			parent.rchild = temp
	
	# Recursive insertion
	def _insert(self, p, key):
		if p is None:	# Base Case
			p = Node(key)
		elif key < p.info:	# Insertion in left subtree
			p.lchild = self._insert(p.lchild, key)
		elif key > p.info: # Insertion in right subtree
			p.rchild = self._insert(p.rchild, key)
		else:	# Base Case
			print(f"{key} is already there")

		return p

	def insert(self, key):
		self.root = self._insert(self.root, key)
	
	def _case_a(self, parent, p):
		if parent is None:	#root node to be deleted
			self.root = None
		elif p == parent.lchild:
			parent.lchild = None
		else:
			parent.rchild = None
	
	def _case_b(self, parent, p):
		# Initialize child
		if p.lchild is not None:	# node to be deleted has left child
			child = p.lchild
		else:					# node to be deleted has right child
			child = p.rchild

		if parent is None:		# node to be deleted is root node
			self.root = child
		elif p == parent.lchild:	#node is left child of its parent
			parent.lchild = child
		else:					# node is right child of its parent
			parent.rchild = child
	
	def _case_c(self, parent, p):
		# Find inorder successor and its parent
		ps = p
		s = p.rchild
		while s.lchild is None:
			ps = s
			s = s.lchild

		p.info = s.info
		if s.lchild is None and s.rchild is None:
			self._case_a(ps, s)
		else:
			self._case_b(ps, s)
	
	# Non Recursive deletion
	def del2(self, key):
		parent = None
		p = self.root

		while p is not None:
			if p.info == key:
				break

			parent = p
			if key < p.info:
				p = p.lchild
			else:
				p = p.rchild

		if p is None:
			print(f"{key} is not in the tree")
		elif p.lchild is not None and p.rchild is not None: # 2 children
			self._case_c(parent, p)
		elif p.lchild is not None: # only left child
			self._case_b(parent, p)
		elif p.rchild is not None: #only right child
			self._case_b(parent, p)
		else:	# no child
			self._case_a(parent, p)
	
	# Non Recursive deletion
	def del1(self, key):
		parent = None
		p = self.root

		while p is not None:
			if p.info == key:
				break

			parent = p
			if key < p.info:
				p = p.lchild
			else:
				p = p.rchild

		if p is None:
			print(f"{key} is not in the tree")
			return

		# Case C : 2 children
		# Find inorder successor and parent
		if p.lchild is not None and p.rchild is not None:
			ps = p
			s = p.rchild

			while s.lchild is not None:
				ps = s
				s = s.lchild
			p.info = s.info
			p = s
			parent = ps

		# Case B and Case A : 1 or no child
		if p.lchild is not None: #Node to be deleted has left child
			child = p.lchild
		else:	# Node to be deleted has right child or no child
			child = p.rchild

		if parent is None:	# Node to be deleted is root node
			self.root = child
		elif p == parent.lchild:	# Node is left child of its parent
			parent.lchild = child
		else:	# Node is right child of its parent
			parent.rchild = child

	# Recursive deletion
	def _del_node(self, p, key):
		if p is None:
			print(f"{key} not found")
			return p

		if key < p.info:	# Delete from left subtree
			p.lchild = self._del_node(p.lchild, key)
		elif(key > p.info):	# Delete from right subtree
			p.rchild = self._del_node(p.rchild, key)
		else:
			# Key to be deleted is found
			if p.lchild is not None and p.rchild is not None: # 2 children
				s = p.rchild
				while s.lchild is not None:
					s = s.lchild
				p.info = s.info
				p.rchild = self._del_node(p.rchild, s.info)
			else:	# 1 child or no child
				if p.lchild is not None: # Only left child
					child = p.lchild
				else:	# Only right child or no child
					child = p.rchild
				p = child

		return p

	def del_node(self, key):
		self.root = self._del_node(self.root, key)
	
	def _display(self, p, level):
		if p is None:
			return

		self._display(p.rchild, level+1)
		print()

		for i in range(0,level):
			print("    ", end='')
		print(p.info, end='')

		self._display(p.lchild, level+1)

	def display(self):
		self._display(self.root, 0)
	
	# Non Recursive search
	def search1(self, key):
		p = self.root

		while p is not None:
			if key < p.info:
				p = p.lchild	# Move to left child
			elif key > p.info:
				p = p.rchild	# Move to right child
			else:	# key found
				return True

		return False
	
	# Recursive search
	def _search(self, p, key):
		if p is None:
			return None	# key not found
		if key < p.info:
			return self._search(p.lchild, key)	# search in left subtree
		if key > p.info:
			return self._search(p.rchild, key)	# search in right subtree
		return p	# key found

	def search(self, key):
		return self._search(self.root, key) is not None
	
	# Non Recursive to find minimum key
	def min1(self):
		if self.is_empty():
			raise Exception("Tree is empty")

		p = self.root
		while p.lchild is not None:
			p = p.lchild

		return p.info
	
	# Non Recursive to find maximum key
	def max1(self):
		if self.is_empty():
			raise Exception("Tree is empty")

		p = self.root
		while p.rchild is not None:
			p = p.rchild

		return p.info
	
	# Recursive to find minimum key
	def _min(self, p):
		if p.lchild is None:
			return p
		return self._min(p.lchild)

	def min(self):
		if self.is_empty():
			raise Exception("Tree is empty")

		return self._min(self.root).info
	
	# Recursive to find maximum key
	def _max(self, p):
		if p.rchild is None:
			return p
		return self._max(p.rchild)

	def max(self):
		if self.is_empty():
			raise Exception("Tree is empty")

		return self._max(self.root).info

if __name__ == '__main__':
	bst = BinarySearchTree()

	try:
		print("Insertion to create the BST :")
		bst.insert1(80)
		bst.insert1(70)
		bst.insert1(65)
		bst.insert1(75)
		bst.insert1(90)
		bst.insert1(85)
		bst.insert1(95)
		bst.display()
		print()
		print("After deleting 95 :")
		bst.del_node(95)
		bst.display()
		print()

		print("Copying BST :")
		bst1 = BinarySearchTree(bst)
		bst1.display()
		print()

		# Search (Iterative) in BST
		print(f"search1(75) : {bst.search1(75)}")
		print()

		# Search (Recursive) in BST
		print(f"search(75) : {bst.search(75)}")
		print()

		print(f"Min key (Iterative) = {bst.min1()}")
		print(f"Min key (Recursive) = {bst.min()}")

		print(f"Max key (Iterative) = {bst.max1()}")
		print(f"Max key (Recursive) = {bst.max()}")

	except Exception as e:
		print(e)
