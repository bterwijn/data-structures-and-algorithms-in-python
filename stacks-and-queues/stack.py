# stack.py : Program to implement stack using list.

class Stack:
	def __init__(self, size=5):
		self.MAX_SIZE = size
		self.list_items = [None] * self.MAX_SIZE
		self.top = -1
	
	def is_empty(self):
		return self.top == -1
	
	def is_full(self):
		return self.top == self.MAX_SIZE-1
	
	def push(self, data):
		if self.is_full():
			print("Stack Overflow")
		else:
			self.top += 1
			self.list_items[self.top] = data
	
	def pop(self):
		if self.is_empty():
			raise Exception("Stack is empty")

		ret_value = self.list_items[self.top]
		self.top -= 1

		return ret_value
	
	def peek(self):
		if self.is_empty():
			raise Exception("Stack is empty")

		return self.list_items[self.top]

	def size(self):
		return self.top+1

	def display(self):
		if self.is_empty():
			print("Stack is empty")
		else:
			i = self.top
			while i >= 0:
				print(self.list_items[i])
				i -= 1

if __name__ == '__main__':
	st = Stack()

	try:
		st.push(1)
		st.push(2)
		st.push(3)
		st.push(4)

		print("Stack Items :")
		st.display()
		print(f"Top Item : {st.peek()}")
		print(f"Total items : {st.size()}")

		print(f"Popped Item : {st.pop()}")
		print("Stack Items :")
		st.display()

		st.push(4)
		st.push(5)

		print("Stack Items :")
		st.display()

		print(f"Popped Item : {st.pop()}")
		print(f"Popped Item : {st.pop()}")
		print(f"Popped Item : {st.pop()}")
		print(f"Popped Item : {st.pop()}")
		print(f"Popped Item : {st.pop()}")

		print("Stack Items :")
		st.display()			
	except Exception as e:
		print(e)
