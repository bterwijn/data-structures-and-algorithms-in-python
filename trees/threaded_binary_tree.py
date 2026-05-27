# threaded_binary_tree.py : Program for Threaded Binary Tree.

class Node:
	def __init__(self,key):
		self.info = key 
		self.lchild = None
		self.rchild = None
		self.lthread = True
		self.rthread = True

class ThreadedBinaryTree:
	def __init__(self):
		self.root = None

	def is_empty(self):
		return self.root==None
	
	def insert(self, key):
		parent = None
		p = self.root

		while p is not None:
			parent = p

			if key < p.info:
				if p.lthread == False:
					p = p.lchild
				else:
					break
			elif key > p.info:
				if p.rthread == False:
					p = p.rchild
				else:
					break
			else:
				print(f"{key} is already there")
				return

		temp = Node(key)

		if parent is None:
			self.root = temp
		elif key < parent.info: # Inserted as left child
			temp.lchild = parent.lchild
			temp.rchild = parent
			parent.lthread = False
			parent.lchild = temp
		else:	# Inserted as right child
			temp.lchild = parent
			temp.rchild = parent.rchild
			parent.rthread = False
			parent.rchild = temp
	
	def inorder(self):
		if self.root is None:
			print("Tree is empty")
			return

		# Find the leftmost node of the tree
		p = self.root

		while p.lthread == False:
			p = p.lchild

		while p is not None:
			print(f"{p.info} ", end='')
			
			if p.rthread == True:
				p = p.rchild
			else:
				p = p.rchild
				while p.lthread == False:
					p = p.lchild
	
	def preorder(self):
		if self.root is None:
			print("Tree is empty")
			return

		p = self.root
		while p is not None:
			print(f"{p.info} ", end='')
			if p.lthread == False:
				p = p.lchild
			elif p.rthread == False:
				p = p.rchild
			else:
				while p is not None and p.rthread==True:
					p = p.rchild

				if p is not None:
					p = p.rchild
	
	def _inorder_predecessor(self, p):
		if p.lthread == True:
			return p.lchild
		else:
			p = p.lchild
			while p.rthread == False:
				p = p.rchild
			return p
	
	def _inorder_successor(self, p):
		if p.rthread == True:
			return p.rchild
		else:
			p = p.rchild
			while p.lthread == False:
				p = p.lchild
			return p
	
	def del_key(self, key):
		parent = None
		p = self.root

		while p is not None:
			if p.info == key:
				break

			parent = p
			if key < p.info:
				if p.lthread == False:
					p = p.lchild
				else:
					break
			else:
				if p.rthread == False:
					p = p.rchild
				else:
					break

		if p is not None and p.info is not key:
			print(f"{key} not found")
			return

		# Case C : 2 children
		if p.lthread==False and p.rthread==False:
			# Find inorder successor and its parent
			ps = p
			s = p.rchild

			while s.lthread == False:
				ps = s
				s = s.lchild
			p.info = s.info
			p = s
			parent = ps

		# Case A : no child
		if p.lthread==True and p.rthread==True:
			if parent is None: # key to be deleted is in root node
				self.root = None
			elif p == parent.lchild:
				parent.lthread = True
				parent.lchild = p.lchild
			else:
				parent.rthread = True
				parent.rchild = p.rchild

			return

		# Case B : 1 child

		# Initialize child
		if p.lthread == False: # Node to be deleted has left child
			child = p.lchild
		else:	# Node to be deleted has right child
			child = p.rchild

		if parent is None: # Node to be deleted is root node
			self.root = child
		elif p == parent.lchild: # Node is left child of its parent
			parent.lchild = child
		else:	# Node is right child of its parent
			parent.rchild = child

		pred = self._inorder_predecessor(p)
		succ = self._inorder_successor(p)

		if p.lthread == False: # If p has left child, right is a thread
			pred.rchild = succ
		else:	# p has right child, left is a thread
			succ.lchild = pred

if __name__ == '__main__':
	threaded_tree = ThreadedBinaryTree()

	threaded_tree.insert(67)
	threaded_tree.insert(34)
	threaded_tree.insert(81)
	threaded_tree.insert(12)
	threaded_tree.insert(45)
	threaded_tree.insert(78)
	threaded_tree.insert(95)
	threaded_tree.insert(20)
	threaded_tree.insert(40)
	threaded_tree.insert(89)
	threaded_tree.insert(98)

	print("Inorder traversal :")
	threaded_tree.inorder()
	print()
	print("Preorder traversal :")
	threaded_tree.preorder()
	print()

	threaded_tree.del_key(81)	# Case C
	print("Inorder traversal after deleting 81 :")
	threaded_tree.inorder()
	print()

	threaded_tree.del_key(45)	# Case B (has only left child)
	print("Inorder traversal after deleting 45 :")
	threaded_tree.inorder()
	print()

	threaded_tree.del_key(12)	# Case B (has only right child)
	print("Inorder traversal after deleting 12 :")
	threaded_tree.inorder()
	print()

	threaded_tree.del_key(40)	# Case A (leaf node)
	print("Inorder traversal after deleting 40 :")
	threaded_tree.inorder()
	print()

	threaded_tree.del_key(67)	# Case C (root node)
	print("Inorder traversal after deleting 67 :")
	threaded_tree.inorder()
	print()
