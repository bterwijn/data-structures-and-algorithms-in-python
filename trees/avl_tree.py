# avl_tree.py : Program for AVL Tree.

class Node:
	def __init__(self,key):
		self.info = key
		self.balance = 0
		self.lchild = None
		self.rchild = None

class AVLTree:
	def __init__(self):
		self.root = None
		self.taller = False
		self.shorter = False

	def is_empty(self):
		return self.root==None

	def display(self):
		self._display(self.root, 0)
		print()

	def _display(self, p, level):
		if p is None:
			return

		self._display(p.rchild, level+1)
		print()

		for i in range(0, level):
			print("    ", end='')
		print(f"{p.info}", end='')

		self._display(p.lchild, level+1)

	def _inorder(self, p):
		if p is None:	#Base Case
			return

		self._inorder(p.lchild)
		print(f"{p.info} ", end='')
		self._inorder(p.rchild)
	
	def inorder(self):
		self._inorder(self.root)
		print()

	def insert(self, key):
		self.root = self._insert(self.root, key)

	def _insert(self, p, key):
		if p is None:				# Base case
			p = Node(key)
			self.taller = True
		elif key < p.info:			# Insertion in left subtree
			p.lchild = self._insert(p.lchild, key)
			if self.taller == True:
				p = self._insertion_left_subtree_check(p)
		elif key > p.info:			# Insertion in right subtree
			p.rchild = self._insert(p.rchild, key)
			if self.taller == True:
				p = self._insertion_right_subtree_check(p)
		else:	# Base case
			print(f"{key} is already there")
			self.taller = False

		return p
	
	def _insertion_left_subtree_check(self, p):
		if p.balance == 0:		# Case L_A : was balanced
			p.balance = 1		# now left heavy
		elif p.balance == -1:	# Case L_B : was right heavy
			p.balance = 0		# now balanced
			self.taller = False
		elif p.balance == 1:	# Case L_C : was left heavy
			p = self._insertion_left_balance(p) # left balancing
			self.taller = False

		return p
	
	def _insertion_left_balance(self, p):
		a = p.lchild
		if a.balance == 1:	# Case L_C1 : Insertion in AL
			p.balance = 0
			a.balance = 0
			p = self._rotate_right(p)
		else:	# Case L_C2 : Insertion in AR
			b = a.rchild

			if b.balance == -1:		# Case L_C2a : Insertion in BR
				p.balance = 0
				a.balance = 1
			elif b.balance == 1:	# Case L_C2b : Insertion in BL
				p.balance = -1
				a.balance = 0
			elif b.balance == 0:	# Case L_C2c : B is the newly inserted node
				p.balance = 0
				a.balance = 0

			b.balance = 0
			p.lchild = self._rotate_left(a)
			p = self._rotate_right(p)

		return p
	
	def _insertion_right_subtree_check(self, p):
		if p.balance == 0:	# Case R_A : was balanced
			p.balance = -1	# now right heavy
		elif p.balance == 1:	# Case R_B : was left heavy
			p.balance = 0		# now balanced
			self.taller = False
		elif p.balance == -1:	# Case R_C : was right heavy
			p = self._insertion_right_balance(p) # right balancing
			self.taller = False

		return p

	def _insertion_right_balance(self, p):
		a = p.rchild
		
		if a.balance == -1:	# Case R_C1 : Insertion in AR
			p.balance = 0
			a.balance = 0
			p = self._rotate_left(p)
		else:	# Case R_C2 : Insertion in AL
			b = a.lchild

			if b.balance == -1:	# Case R_C2a : Insertion in BR
				p.balance = 1
				a.balance = 0
			elif b.balance == 1: # Case R_C2b : Insertion in BL
				p.balance = 0
				a.balance = -1
			elif b.balance == 0: # Case R_C2c : B is the newly inserted node
				p.balance = 0
				a.balance = 0

			b.balance = 0
			p.rchild = self._rotate_right(a)
			p = self._rotate_left(p)

		return p
	
	def _rotate_right(self, p):
		a = p.lchild			# A is left child of P
		p.lchild = a.rchild		# Right child of A becomes left child of P	
		a.rchild = p			# P becomes right child of A
		return a				# A is the new root of the subtree initially rooted at P

	def _rotate_left(self, p):
		a = p.rchild			# A is right child of P
		p.rchild = a.lchild		# Left child of A becomes right child of P
		a.lchild = p			# P becomes left child of A
		return a				# A is the new root of the subtree initially rooted at P
	
	def del_key(self, key):
		self.root = self._del_key(self.root, key)
	
	def _del_key(self, p, key):
		if p is None:		# Base case
			print(f"{key} not found")
			self.shorter = False
			return p

		if key < p.info:	# Delete from left subtree
			p.lchild = self._del_key(p.lchild, key)
			if self.shorter == True:
				p = self._deletion_left_subtree_check(p)
		elif key > p.info:	# Delete from right subtree
			p.rchild = self._del_key(p.rchild, key)
			if self.shorter == True:
				p = self._deletion_right_subtree_check(p)
		else:	# key to be deleted is found, Base case	
			if p.lchild is not None and p.rchild is not None: #2 children
				succ = p.rchild
				while succ.lchild is not None:
					succ = succ.lchild
				p.info = succ.info
				p.rchild = self._del_key(p.rchild, succ.info)
				if self.shorter == True:
					p = self._deletion_right_subtree_check(p)
			else:	# 1 child or no child
				if p.lchild is not None:	# Only left child
					p = p.lchild
				else:	# Only right child or no child
					p = p.rchild
				self.shorter = True

		return p
	
	def _deletion_left_subtree_check(self, p):
		if p.balance == 0:		# Case L_A : was balanced
			p.balance = -1		# now right heavy
			self.shorter = False
		elif p.balance == 1:	# Case L_B : was left heavy
			p.balance = 0		# now balanced
		elif p.balance == -1:	# Case L_C : was right heavy
			p = self._deletion_right_balance(p) # right balancing

		return p
	
	def _deletion_right_balance(self, p):
		a = p.rchild
		if a.balance == 0:		# Case L_C1
			a.balance = 1
			self.shorter = False
			p = self._rotate_left(p)
		elif a.balance == -1:	# Case L_C2
			p.balance = 0
			a.balance = 0
			p = self._rotate_left(p)
		else:	# Case L_C3
			b = a.lchild

			if b.balance == 0:		# Case L_C3a
				p.balance = 0
				a.balance = 0
			elif b.balance == 1:	# Case L_C3b
				p.balance = 0
				a.balance = -1
			elif b.balance == -1:	# Case L_C3c
				p.balance = 1
				a.balance = 0

			b.balance = 0
			p.rchild = self._rotate_right(a)
			p = self._rotate_left(p)

		return p
	
	def _deletion_right_subtree_check(self, p):
		if p.balance == 0:		# Case R_A : was balanced
			p.balance = 1		# now left heavy
			self.shorter = False
		elif p.balance == -1:	# Case R_B : was right heavy
			p.balance = 0		# now balanced
		elif p.balance == 1:	# Case R_C : was left heavy
			p = self._deletion_left_balance(p)	# left balancing

		return p
	
	def _deletion_left_balance(self, p):
		a = p.lchild
		if a.balance == 0:		# Case R_C1
			a.balance = -1
			self.shorter = False
			p = self._rotate_right(p)
		elif a.balance == 1:	# Case R_C2
			p.balance = 0
			a.balance = 0
			p = self._rotate_right(p)
		else:	# Case R_C3
			b = a.rchild

			if b.balance == 0:		# Case R_C3a
				p.balance = 0
				a.balance = 0
			elif b.balance == 1:	# Case R_C3b
				p.balance = -1
				a.balance = 0
			elif b.balance -1:		# Case R_C3c
				p.balance = 0
				a.balance = 1

			b.balance = 0
			p.lchild = self._rotate_left(a)
			p = self._rotate_right(p)

		return p

if __name__ == '__main__':
	avl_tree = AVLTree()

	avl_tree.insert(50)
	print("Tree after inserting 50")
	avl_tree.display()
	print()

	avl_tree.insert(40)
	print("Tree after inserting 40")
	avl_tree.display()
	print()

	avl_tree.insert(35)
	print("Tree after insertiing 35")
	avl_tree.display()
	print()

	avl_tree.insert(58)
	print("Tree after inserting 58")
	avl_tree.display()
	print()

	avl_tree.insert(48)
	print("Tree after inserting 48")
	avl_tree.display()
	print()

	avl_tree.insert(42)
	print("Tree after inserting 42")
	avl_tree.display()
	print()

	avl_tree.insert(60)
	print("Tree after inserting 60")
	avl_tree.display()
	print()

	avl_tree.insert(30)
	print("Tree after inserting 30")
	avl_tree.display()
	print()

	avl_tree.insert(33)
	print("Tree after inserting 33")
	avl_tree.display()
	print()

	avl_tree.insert(25)
	print("Tree after inserting 25")
	avl_tree.display()
	print()

	avl_tree.del_key(60)
	print("Tree after deleting 60")
	avl_tree.display()
	print()

	avl_tree.del_key(48)
	print("Tree after deleting 48")
	avl_tree.display()
	print()

	avl_tree.del_key(25)
	print("Tree after deleting 25")
	avl_tree.display()
	print()

	avl_tree.del_key(30)
	print("Tree after deleting 30")
	avl_tree.display()
	print()

	avl_tree.del_key(35)
	print("Tree after deleting 35")
	avl_tree.display()
	print()

	avl_tree.del_key(33)
	print("Tree after deleting 33")
	avl_tree.display()
	print()

	avl_tree.del_key(58)
	print("Tree after deleting 58")
	avl_tree.display()
	print()
