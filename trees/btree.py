# btree.py : Program for B tree.

from math import ceil

class Node:
	def __init__(self,size):
		self.key = [None] * (size+1)
		self.child = [None] * (size+1)
		self.num_keys = 0	

class NodeHolder:
	def __init__(self,x):
		self.value = x

class IntHolder:
	def __init__(self,n):
		self.value = n

class BTree:
	def __init__(self):
		self.root = None
		self.M = 5 # Order of B tree
		self.MAX = self.M-1 # Maximum number of permissible keys in a node
		# self.MIN = (M%2==0)?((M//2)-1):(((M+1)//2)-1) # Minimum number of permissible keys in a node except root
		self.MIN = ceil(self.M/2) - 1		

	def is_empty(self):
		return self.root == None
		
	def insert(self, key):
		ikey = IntHolder(0)
		ikey_rchild = NodeHolder(None)

		self._taller = self._insert(key, self.root, ikey, ikey_rchild)

		if self._taller: # tree grown in height, new root is created
			temp = Node(self.MAX)
			temp.child[0] = self.root
			temp.key[1] = ikey.value
			temp.child[1] = ikey_rchild.value
			temp.num_keys = 1
			self.root = temp
	
	def _insert(self, key, p, ikey, ikey_rchild):
		if p is None: # First Base case : key not found
			ikey.value = key
			ikey_rchild.value = None
			return True

		n = IntHolder(0)
		if self._search_node(key, p, n) == True: # Second Base case : key found
			print("Key already present in the tree")
			return False	# No need to insert the key

		flag = self._insert(key, p.child[n.value], ikey, ikey_rchild)

		if flag == True:
			if p.num_keys < self.MAX:
				self._insert_by_shift(p, n.value, ikey.value, ikey_rchild.value)
				return False	#Insertion over
			else:
				self._split(p, n.value, ikey, ikey_rchild)
				return True # Insertion not over : Median key yet to be inserted

		return False

	def search(self, key):
		if self._search(key, self.root) is None:
			return False
		return True
	
	def _search(self, key, p):
		if p is None:
			return None # Base case 1 : key is not present in the tree

		n = IntHolder(0)
		if self._search_node(key, p, n)==True: # Base case 2 : key is found in node p
			return p

		return self._search(key, p.child[n.value]) # Recursive case : Search in node p.child[n]
	
	def _search_node(self, key, p, n):
		if key < p.key[1]:		# key is less than leftmost key
			n.value = 0
			return False

		n.value = p.num_keys
		while key<p.key[n.value] and n.value>1:
			n.value -= 1

		if key == p.key[n.value]:
			return True
		else:
			return False

	def _insert_by_shift(self, p, n, ikey, ikey_rchild):
		i = p.num_keys
		while i > n:
			p.key[i+1] = p.key[i]
			p.child[i+1] = p.child[i]
			i -= 1

		p.key[n+1] = ikey
		p.child[n+1] = ikey_rchild
		p.num_keys += 1
	
	def _split(self, p, n, ikey, ikey_rchild):
		if n == self.MAX:
			last_key = ikey.value
			last_child = ikey_rchild.value
		else:
			last_key = p.key[self.MAX]
			last_child = p.child[self.MAX]

			i = p.num_keys-1
			while i > n:
				p.key[i+1] = p.key[i]
				p.child[i+1] = p.child[i]
				i -= 1

			p.key[i+1] = ikey.value
			p.child[i+1] = ikey_rchild.value

		d = (self.M+1)//2
		median_key = p.key[d]
		new_node = Node(self.MAX)

		i = 1
		j = d+1
		while j <= self.MAX:
			new_node.key[i] = p.key[j]
			new_node.child[i] = p.child[j]
			i += 1
			j += 1

		new_node.key[i] = last_key
		new_node.child[i] = last_child
		new_node.num_keys = self.M-d # Number of keys in the right splitted node

		new_node.child[0] = p.child[d]
		p.num_keys = d-1 # Number of keys in the left splitted node

		ikey.value = median_key
		ikey_rchild.value = new_node
	
	def del_key(self, key):
		if self.root is not None:
			self._del_key(key, self.root)

			# If tree becomes shorter, root is changed
			if self.root is not None and self.root.num_keys==0:
				self.root = self.root.child[0]
		else:
			print("Tree is empty")
	
	def _del_key(self, key, p):
		n = IntHolder(0)

		if p is None:	# reached leaf node, key does not exist
			print("Key {key} not found")
		else:
			if self._search_node(key, p, n): # If found in current node p
				if p.child[n.value] is None: # Node p is a leaf node
					self._del_by_shift(p, n.value)
				else:	# Node p is a non leaf node
					succ = p.child[n.value] # refers to the right subtree
					while succ.child[0] is not None: # move down till leaf node arrives
						succ = succ.child[0]
					p.key[n.value] = succ.key[1]
					self._del_key(succ.key[1], p.child[n.value])
			else:	# Not found in current node p
				self._del_key(key, p.child[n.value])

			if p.child[n.value] is not None: # If p is not a leaf node
				if p.child[n.value].num_keys < self.MIN: # Check underflow in p.child[n]
					self._restore(p, n.value)
	
	def _del_by_shift(self, p, n):
		i = n+1
		while i <= p.num_keys:
			p.key[i-1] = p.key[i]
			p.child[i-1] = p.child[i]
			i += 1

		p.num_keys -= 1
	
	def _restore(self, p, n):
		if n!=0 and p.child[n-1].num_keys > self.MIN:
			self._borrow_left(p, n)
		elif n!=p.num_keys and p.child[n+1].num_keys > self.MIN:
			self._borrow_right(p, n)
		else:
			if n==0:	# If underflow node is leftmost node
				combine(p, n+1) # combine nth child of p with its right sibling
			else:
				self._combine(p, n) # combine nth child of p with its left sibling
	
	def _borrow_left(self, p, n):
		u = p.child[n]	# underflow node
		ls = p.child[n-1]	# left sibling of node u

		# Shift all the keys and children in underflow node u one position right
		i = u.num_keys
		while i > 0:
			u.key[i+1] = u.key[i]
			u.child[i+1] = u.child[i]
			i -= 1
		u.child[1] = u.child[0]

		# Move the separator key from parent node p to underflow node u
		u.key[1] = p.key[n]
		
		u.num_keys += 1

		# Move the rightmost key of node ls to the parent node p
		p.key[n] = ls.key[ls.num_keys]
		
		# Rightmost child of ls becomes leftmost child of node u
		u.child[0] = ls.child[ls.num_keys]
		
		ls.num_keys -= 1
	
	def _borrow_right(self, p, n):
		u = p.child[n]	# underflow node
		rs = p.child[n+1]	# right sibling of node u

		# Move the separator key from the parent node p to the underflow node u
		u.num_keys += 1
		u.key[u.num_keys] = p.key[n+1]

		# Leftmost child of node rs becomes the rightmost child of node u
		u.child[u.num_keys] = rs.child[0]

		# Move the leftmost key from node rs to parent node p
		p.key[n+1] = rs.key[1]
		rs.num_keys -= 1

		# Shift all the keys and children of node rs one position left
		rs.child[0] = rs.child[1]
		i = 1
		while i <= rs.num_keys:
			rs.key[i] = rs.key[i+1]
			rs.child[i] = rs.child[i+1]
			i += 1
	
	def _combine(self, p, m):
		x = p.child[m]
		y = p.child[m-1]

		# Move the separator key from parent node p to node y
		y.num_keys += 1
		y.key[y.num_keys] = p.key[m]

		# Shift all the keys and children in node p one position left to fill the gap
		i = m
		while i < p.num_keys:
			p.key[i] = p.key[i+1]
			p.child[i] = p.child[i+1]
			i += 1

		p.num_keys -= 1

		# Leftmost child of x becomes rightmost child of y
		y.child[y.num_keys] = x.child[0]

		# Insert all the keys and children of node x at the end of node y
		i = 1
		while i <= x.num_keys:
			y.num_keys += 1
			y.key[y.num_keys] = x.key[i]
			y.child[y.num_keys] = x.child[i]
			i += 1
	
	def inorder(self):
		self._inorder(self.root)
	
	def _inorder(self, p):
		if p is not None:
			for i in range(0,p.num_keys):
				self._inorder(p.child[i])
				print(f"{p.key[i+1]} ", end='')

			self._inorder(p.child[i+1])
	
	def display(self):
		self._display(self.root, 0)
	
	def _display(self, p, spaces):
		if p is not None:
			i = 1
			while i <= spaces:
				print(" ", end='')
				i += 1

			i = 1
			while i <= p.num_keys:
				print(f"{p.key[i]} ", end='')
				i += 1
			print()

			i = 0
			while i <= p.num_keys:
				self._display(p.child[i], spaces+10)
				i += 1

if __name__ == '__main__':
	btree = BTree()

	print("Tree after inserting 10")
	btree.insert(10)
	btree.display()
	print()

	print("Tree after inserting 40")
	btree.insert(40)
	btree.display()
	print()

	print("Tree after inserting 30")
	btree.insert(30)
	btree.display()
	print()

	print("Tree after inserting 35")
	btree.insert(35)
	btree.display()
	print()

	print("Tree after inserting 20")
	btree.insert(20)
	btree.display()
	print()

	print("Tree after inserting 15")
	btree.insert(15)
	btree.display()
	print()

	print("Tree after inserting 50")
	btree.insert(50)
	btree.display()
	print()

	print("Tree after inserting 28")
	btree.insert(28)
	btree.display()
	print()

	print("Tree after inserting 25")
	btree.insert(25)
	btree.display()
	print()

	print("Tree after inserting 5")
	btree.insert(5)
	btree.display()
	print()

	print("Tree after inserting 60")
	btree.insert(60)
	btree.display()
	print()

	print("Tree after inserting 19")
	btree.insert(19)
	btree.display()
	print()

	print("Tree after inserting 12")
	btree.insert(12)
	btree.display()
	print()

	print("Tree after inserting 38")
	btree.insert(38)
	btree.display()
	print()

	print("Tree after inserting 27")
	btree.insert(27)
	btree.display()
	print()

	print("Tree after inserting 90")
	btree.insert(90)
	btree.display()
	print()

	print("Tree after inserting 45")
	btree.insert(45)
	btree.display()
	print()

	print("Tree after inserting 48")
	btree.insert(48)
	btree.display()
	print()

	print("Tree after deleting 28")
	btree.del_key(28)
	btree.display()
	print()

	print("Tree after deleting 40")
	btree.del_key(40)
	btree.display()
	print()

	print("Tree after deleting 15")
	btree.del_key(15)
	btree.display()
	print()

	# Search in B-tree
	print(f"search(48) : {btree.search(48)}")

	print(f"search(15) : {btree.search(15)}")
	
	print("Inorder traversal :")
	btree.inorder()
	print()
