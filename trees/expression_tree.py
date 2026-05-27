# expression_tree.py : Program for Expression Tree.

class Node:
	def __init__(self,value):
		self.info = value
		self.lchild = None
		self.rchild = None

class ExpressionTree:
	def __init__(self):
		self.root = None
	
	def _is_operator(self, c):
		if c=='+' or c=='-' or c=='*' or c=='/':
			return True
		return False
	
	def build_tree(self, postfix):
		tree_stack = [] # list as stack

		for i in range(0, len(postfix)):
			if self._is_operator(postfix[i]):
				t = Node(postfix[i])
				t.rchild = tree_stack.pop()
				t.lchild = tree_stack.pop()
				tree_stack.append(t)
			else:	# operand
				t = Node(postfix[i])
				tree_stack.append(t)

		self.root = tree_stack.pop()

	def _preorder(self, p):
		if p is None:	# Base case
			return

		print(p.info, end='')
		self._preorder(p.lchild)
		self._preorder(p.rchild)

	def prefix(self):
		self._preorder(self.root)
		print()
	
	def _postorder(self, p):
		if p is None:	# Base case
			return

		self._postorder(p.lchild)
		self._postorder(p.rchild)
		print(p.info, end='')

	def postfix(self):
		self._postorder(self.root)
		print()

	def _inorder(self, p):
		if p is None:	# Base case
			return

		if self._is_operator(p.info):
			print("(", end='')

		self._inorder(p.lchild)
		print(p.info, end='')
		self._inorder(p.rchild)

		if self._is_operator(p.info):
			print(")", end='')

	def parenthesized_infix(self):
		self._inorder(self.root)
		print()
	
	def _display(self, p, level):
		if p is None:
			return

		self._display(p.rchild, level+1)
		print()

		for i in range(0, level):
			print("    ", end='')
		print(p.info, end='')

		self._display(p.lchild, level+1)

	def display(self):
		self._display(self.root, 0)
		print()
	
	def _evaluate(self, p):
		value = 0
		
		if not self._is_operator(p.info):
			return ord(p.info) - 48

		left_value = self._evaluate(p.lchild)
		right_value = self._evaluate(p.rchild)

		if p.info == '+':
			value = left_value + right_value
		elif p.info == '-':
			value = left_value - right_value
		elif p.info == '*':
			value = left_value * right_value
		elif p.info == '/':
			value = left_value / right_value
		
		return value

	def evaluate(self):
		if self.root is None:
			return 0

		return self._evaluate(self.root)

if __name__ == '__main__':
	exp_tree = ExpressionTree()

	postfix = "54+12*3*-"

	exp_tree.build_tree(postfix)
	exp_tree.display()

	print("Prefix : ", end='')
	exp_tree.prefix()

	print("Postfix : ", end='')
	exp_tree.postfix()

	print("Infix : ", end='')
	exp_tree.parenthesized_infix()

	print(f"Evaluated Value : {exp_tree.evaluate()}")
