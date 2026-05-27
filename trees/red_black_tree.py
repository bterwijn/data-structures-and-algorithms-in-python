# red_black_tree.py : Program for Red Black Tree.

from enum import Enum

class Color(Enum):
	BLACK = 0
	RED = 1

class Node:
	def __init__(self,key):
		self.info = key
		self.lchild = None
		self.rchild = None
		self.parent = None
		self.color = Color.BLACK

class RedBlackTree:
	def __init__(self):
		self.sentinel = Node(-1)
		self.sentinel.color = Color.BLACK
		self.root = self.sentinel
	
	def insert(self, key):
		parent = self.sentinel
		p = self.root

		while p is not self.sentinel:
			parent = p
			if key < p.info:
				p = p.lchild
			elif key > p.info:
				p = p.rchild
			else:
				print(f"{key} is already there")
				return

		temp = Node(key)
		temp.lchild = self.sentinel
		temp.rchild = self.sentinel
		temp.color = Color.RED
		temp.parent = parent

		if parent == self.sentinel:
			self.root = temp
		elif temp.info < parent.info:
			parent.lchild = temp
		else:
			parent.rchild = temp

		self._insertion_balance(temp)
	
	def _insertion_balance(self, n):
		while n.parent.color == Color.RED:
			parent = n.parent
			grand_parent = parent.parent

			if parent == grand_parent.lchild:
				uncle = grand_parent.rchild
				if uncle.color == Color.RED: # Case L_1
					parent.color = Color.BLACK
					uncle.color = Color.BLACK
					grand_parent.color = Color.RED
					n = grand_parent
				else:	# uncle is black
					if n == parent.rchild: # Case L_2a
						self._rotate_left(parent)
						n = parent
						parent = n.parent

					parent.color = Color.BLACK # Case L_2b
					grand_parent.color = Color.RED
					self._rotate_right(grand_parent)
			else:
				if parent == grand_parent.rchild:
					uncle = grand_parent.lchild
					if uncle.color == Color.RED: # Case R_1
						parent.color = Color.BLACK
						uncle.color = Color.BLACK
						grand_parent.color = Color.RED
						n = grand_parent
					else:	# uncle is black
						if n == parent.lchild:	# Case R_2a
							self._rotate_right(parent)
							n = parent
							parent = n.parent

						parent.color = Color.BLACK # Case R_2b
						grand_parent.color = Color.RED
						self._rotate_left(grand_parent)

		self.root.color = Color.BLACK

	def _get_successor(self, location):
		p = location.rchild
		while p.lchild is not self.sentinel:
			p = p.lchild
		
		return p

	def _find(self, key):
		if self.root == self.sentinel: # Tree is empty
			location = self.sentinel
			return None

		if key == self.root.info: # key is at root
			location = self.root
			return location

		# Initialize p
		if key < self.root.info:
			p = self.root.lchild
		else:
			p = self.root.rchild

		while p is not self.sentinel:
			if key == p.info:
				location = p
				return location

			if key < p.info:
				p = p.lchild
			else:
				p = p.rchild

		location = sentinel		# key not found
		return None
	
	def del_key(self, key):
		p = self._find(key)

		if p is None:
			print("Key not present")
			return
	
		if p.lchild is not self.sentinel and p.rchild is not self.sentinel:
			succ = self._get_successor(p)
			p.info = succ.info
			p = succ

		if p.lchild is not self.sentinel:
			child = p.lchild
		else:
			child = p.rchild

		child.parent = p.parent

		if p.parent == self.sentinel:
			self.root = child
		elif p == p.parent.lchild:
			p.parent.lchild = child
		else:
			p.parent.rchild = child

		if child == self.root:
			child.color = Color.BLACK
		elif p.color == Color.BLACK: # black node
			if child is not self.sentinel: # one child which is red
				child.color = Color.BLACK
			else:	# no child
				self._deletion_balance(child)
	
	def _deletion_balance(self, n):
		while n is not self.root:
			if n == n.parent.lchild:
				sib = n.parent.rchild

				if sib.color == Color.RED: # Case L_1
					sib.color = Color.BLACK
					n.parent.color = Color.RED
					self._rotate_left(n.parent)
					sib = n.parent.rchild #new sibling

				if sib.lchild.color==Color.BLACK and sib.rchild.color==Color.BLACK:
					sib.color = Color.RED
					if n.parent.color == Color.RED: # Case L_2a
						n.parent.color = Color.BLACK
						return
					else:
						n = n.parent # Case L_2b
				else:
					if sib.rchild.color == Color.BLACK: # Case L_3a
						sib.lchild.color = Color.BLACK
						sib.color = Color.RED
						self._rotate_right(sib)
						sib = n.parent.rchild
					sib.color = n.parent.color # Case L_3b
					n.parent.color = Color.BLACK
					sib.rchild.color = Color.BLACK
					self._rotate_left(n.parent)
					return
			else:
				sib = n.parent.lchild
				if sib.color == Color.RED: #Case R_1
					sib.color = Color.BLACK
					n.parent.color = Color.RED
					self._rotate_right(n.parent)
					sib = n.parent.lchild

				if sib.rchild.color==Color.BLACK and sib.lchild.color==Color.BLACK:
					sib.color = Color.RED
					if n.parent.color == Color.RED: # Case R_2a
						n.parent.color = Color.BLACK
						return
					else:
						n = n.parent # Case R_2b
				else:
					if sib.lchild.color == Color.BLACK: # Case R_3a
						sib.rchild.color = Color.BLACK
						sib.color = Color.RED
						self._rotate_left(sib)
						sib = n.parent.lchild
					
					sib.color = n.parent.color # Case R_3b
					n.parent.color = Color.BLACK
					sib.lchild.color = Color.BLACK
					self._rotate_right(n.parent)
					return
	
	def _rotate_right(self, p):
		a = p.lchild	# A is left child of P
		p.lchild = a.rchild # Right child of A becomes left child of P

		if a.rchild is not self.sentinel:
			a.rchild.parent = p
		a.parent = p.parent

		if p.parent == self.sentinel:
			self.root = a
		elif p == p.parent.rchild:
			p.parent.rchild = a
		else:
			p.parent.lchild = a

		a.rchild = p	# P becomes right child of A
		p.parent = a

	def _rotate_left(self, p):
		a = p.rchild	# A is right child of P
		p.rchild = a.lchild # Left child of A becomes right child of P

		if a.lchild is not self.sentinel:
			a.lchild.parent = p
		a.parent = p.parent

		if p.parent == self.sentinel:
			self.root = a
		elif p == p.parent.lchild:
			p.parent.lchild = a
		else:
			p.parent.rchild = a

		a.lchild = p	# P becomes left child of A
		p.parent = a
		
	def _inorder(self, p):
		if p is not self.sentinel:
			self._inorder(p.lchild)
			print(p.info)
			self._inorder(p.rchild)

	def inorder(self):
		self._inorder(self.root)

	def _display(self, p, level):
		if p is not self.sentinel:
			self._display(p.rchild, level+1)
			print()

			for i in range(0,level):
				print("    ", end='')
			print(p.info, end='')
			if p.color == Color.RED:
				print("^", end='')
			else:
				print("*", end='')
			
			self._display(p.lchild, level+1)

	def display(self):
		self._display(self.root, 1)

if __name__ == '__main__':
	rb_tree = RedBlackTree()

	print("Tree after inserting 50")
	rb_tree.insert(50)
	rb_tree.display()
	print()

	print("Tree after inserting 60")
	rb_tree.insert(60)
	rb_tree.display()
	print()

	print("Tree after inserting 70")
	rb_tree.insert(70)
	rb_tree.display()
	print()

	rb_tree.insert(40)
	print("Tree after inserting 40")
	rb_tree.display()
	print()

	print("Tree after inserting 55")
	rb_tree.insert(55)
	rb_tree.display()
	print()

	print("Tree after inserting 75")
	rb_tree.insert(75)
	rb_tree.display()
	print()

	print("Tree after inserting 53")
	rb_tree.insert(53)
	rb_tree.display()
	print()

	print("Tree after inserting 54")
	rb_tree.insert(54)
	rb_tree.display()
	print()

	print("Tree after inserting 30")
	rb_tree.insert(30)
	rb_tree.display()
	print()

	print("Tree after inserting 45")
	rb_tree.insert(45)
	rb_tree.display()
	print()

	print("Tree after inserting 35")
	rb_tree.insert(35)
	rb_tree.display()
	print()

	print("Tree after inserting 51")
	rb_tree.insert(51)
	rb_tree.display()
	print()

	print("Tree after deleting 55")
	rb_tree.del_key(55)
	rb_tree.display()
	print()

	print("Tree after deleting 50")
	rb_tree.del_key(50)
	rb_tree.display()
	print()

	print("Tree after deleting 75")
	rb_tree.del_key(75)
	rb_tree.display()
	print()

	print("Tree after deleting 45")
	rb_tree.del_key(45)
	rb_tree.display()
	print()		
