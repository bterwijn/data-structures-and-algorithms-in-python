# stackl.py : Program to implement stack using linked list.

class Node:
	def __init__(self,value):
		self.info = value 
		self.link = None

class StackL:
	def __init__(self):
		self.top = None
    
	def is_empty(self):
		return self.top == None
    
	def push(self, data):
		temp = Node(data)
		if self.is_empty() is not True:
			temp.link = self.top

		self.top = temp
    
	def pop(self):
		if self.is_empty():
			raise Exception("Stack is empty")
		else:
			ret_value = self.top.info
			self.top = self.top.link

		return ret_value
    
	def peek(self):
		if self.is_empty():
			raise Exception("Stack is empty")

		return self.top.info

	def display(self):
		if self.is_empty() is not True:
			p = self.top
			while p is not None:
				print(p.info)
				p = p.link
		else:
			print("Stack is empty")

	def size(self):
		count = 0

		p = self.top
		while p is not None:
			count += 1
			p = p.link

		return count

if __name__ == '__main__':
	st = StackL()

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
