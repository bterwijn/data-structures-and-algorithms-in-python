# binary_tree.py : Program for Binary Tree.

from collections import deque

class Node:
	def __init__(self,value):
		self.info = value 
		self.lchild = None
		self.rchild = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def is_empty(self):
		return root==None

	def create_tree(self):
		self.root = Node('P')
		self.root.lchild = Node('Q')
		self.root.rchild = Node('R')

		self.root.lchild.lchild = Node('A')
		self.root.lchild.rchild = Node('B')

		self.root.rchild.lchild = Node('X')

	def _preorder(self, p):
		if p is None:	# Base case
			return

		print(f"{p.info} ", end='')
		self._preorder(p.lchild)
		self._preorder(p.rchild)

	def preorder(self):
		self._preorder(self.root)
		print()
	
	def _inorder(self, p):
		if p is None:	# Base case
			return

		self._inorder(p.lchild)
		print(f"{p.info} ", end='')
		self._inorder(p.rchild)

	def inorder(self):
		self._inorder(self.root)
		print()
	
	def _postorder(self, p):
		if p is None:	# Base case
			return

		self._postorder(p.lchild)
		self._postorder(p.rchild)
		print(f"{p.info} ", end='')

	def postorder(self):
		self._postorder(self.root)
		print()

	def levelorder(self):
		qu = deque()

		qu.append(self.root)
		while len(qu) != 0:
			p = qu.popleft()
			print(f"{p.info} ", end='')

			if p.lchild is not None:
				qu.append(p.lchild)

			if p.rchild is not None:
				qu.append(p.rchild)

		print()
	
	def _height(self, p):
		if p is None:	# Base case
			return 0

		h_left = self._height(p.lchild)
		h_right = self._height(p.rchild)

		if h_left > h_right:
			return 1+h_left
		else:
			return 1+h_right

	def height(self):
		return self._height(self.root)
	
	# Non recursive Preorder traversal
	def nrec_preorder(self):
		st = [] # list as stack
		p = self.root

		if p is not None:
			st.append(p)
			while len(st) != 0:
				p = st.pop()
				print(f"{p.info} ", end='')
				if p.rchild is not None:
					st.append(p.rchild)
				if p.lchild is not None:
					st.append(p.lchild)

			print()
		else:
			print("Tree is empty")
	
	# Non recursive Inorder traversal
	def nrec_inorder(self):
		st = [] # list as stack
		p = self.root

		if p is not None:
			while True:
				while p.lchild is not None:
					st.append(p)
					p = p.lchild

				while p.rchild is None:
					print(f"{p.info} ", end='')
					if len(st) == 0:
						print()
						return
					p = st.pop()

				print(f"{p.info} ", end='')
				p = p.rchild
		else:
			print("Tree is empty")

	# Non recursive Postorder traversal
	def nrec_postorder(self):
		st = [] # list as stack
		p = self.root
		visited = self.root

		if p is not None:
			while True:
				while p.lchild is not None:
					st.append(p)
					p = p.lchild

				while p.rchild is None or p.rchild==visited:
					print(f"{p.info} ", end='')
					visited = p
					if len(st) == 0:
						print()
						return
					p = st.pop()
				st.append(p)
				p = p.rchild
		else:
			print("Tree is empty")
	
	def _display(self, p, level):
		if p is None:
			return

		self._display(p.rchild, level+1)
		print()

		for i in range(0,level):
			print("    ", end='')
		print(f"{p.info}", end='')

		self._display(p.lchild, level+1)

	def display(self):
		self._display(self.root, 0)
		print()
	
	# Creation of binary tree from inorder and preorder traversal
	def _construct(self, inr, pre, num):	
		if num == 0:
			return None

		temp = Node(pre[0])

		if num == 1:	# if only one node in tree
			return temp
	
		i = 0
		while inr[i] != pre[0]:
			i += 1

		# Number of nodes in its left subtree is i
		# For left subtree
		temp.lchild = self._construct(inr, pre[1:], i)

		# For right subtree
		j = 1
		while j <= i+1:
			j += 1

		temp.rchild = self._construct(inr[i+1:], pre[j-1:], num-i-1)

		return temp

	def construct(self, inr, pre):
		self.root = self._construct(inr, pre, len(inr))
	
	# Creation of binary tree from inorder and postorder traversal
	def _construct1(self, inr, post, num):
		if num == 0:
			return None

		i = 1
		while i < num:
			i += 1

		temp = Node(post[i-1])

		if num == 1:	# if only one node in tree
			return temp
		
		k = 0
		while inr[k] is not post[i-1]:
			k += 1

		# Now k denotes the number of nodes in left subtree
		# For left subtree
		temp.lchild = self._construct1(inr, post, k)

		# For right subtree
		j = 1
		while j <= k:
			j += 1

		temp.rchild = self._construct1(inr[k+1:], post[j-1:], num-k-1)

		return temp

	def construct1(self, inr, post):
		self.root = self._construct1(inr, post, len(inr))

if __name__ == '__main__':
	bn_tree = BinaryTree()

	bn_tree.create_tree()
	bn_tree.display()
	print()

	print("Preorder traversal :")
	bn_tree.preorder()
	
	print("Inorder traversal :")
	bn_tree.inorder()

	print("Postorder traversal :")
	bn_tree.postorder()

	print("Level order traversal :")
	bn_tree.levelorder()

	print(f"Height = {bn_tree.height()}")
	
	print("Non Recursive Preorder traversal :")
	bn_tree.nrec_preorder()
	
	print("Non Recursive Inorder traversal :")
	bn_tree.nrec_inorder()

	print("Non Recursive Postorder traversal :")
	bn_tree.nrec_postorder()
	
	inorder_traversal = "GDHBEIACJFK"

	preorder_traversal = "ABDGHEICFJK"
	bn_tree1 = BinaryTree()
	print(f"Creation of binary tree from Inorder = {inorder_traversal}, Preorder = {preorder_traversal}")
	bn_tree1.construct(inorder_traversal, preorder_traversal)
	bn_tree1.display()
	print()
	
	postorder_traversal = "GHDIEBJKFCA"
	bn_tree2 = BinaryTree()
	print(f"Creation of binary tree from Inorder = {inorder_traversal}, Postorder = {postorder_traversal}")
	bn_tree2.construct1(inorder_traversal, postorder_traversal)
	bn_tree2.display()
	print()
