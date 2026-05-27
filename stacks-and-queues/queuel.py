# queuel.py : Program to implement queue using linked list.

class Node:
	def __init__(self,value):
		self.info = value 
		self.link = None

class QueueL:
	def __init__(self):
		self.front = None
		self.rear = None

	def is_empty(self):
		return self.front == None

	def enqueue(self, data):
		temp = Node(data)

		if self.is_empty(): #If queue is empty
			self.front = temp
		else:
			self.rear.link = temp

		self.rear = temp

	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		else:
			ret_value = self.front.info
			self.front = self.front.link

		return ret_value

	def peek(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		return self.front.info

	def display(self):
		if self.is_empty() is not True:
			p = self.front
			while p is not None:
				print(p.info)
				p = p.link
		else:
			print("Queue is empty")

	def size(self):
		count = 0

		p = self.front
		while p is not None:
			count += 1
			p = p.link

		return count

if __name__ == '__main__':
	qu = QueueL()

	try:
		qu.enqueue(1)
		qu.enqueue(2)
		qu.enqueue(3)
		qu.enqueue(4)

		print("Queue Items :")
		qu.display()
		print(f"Front Item : {qu.peek()}")
		print(f"Total items : {qu.size()}")

		print(f"Deleted Item : {qu.dequeue()}")
		print("Queue Items :")
		qu.display()

		qu.enqueue(5)

		print("Queue Items :")
		qu.display()

		print(f"Deleted Item : {qu.dequeue()}")
		print(f"Deleted Item : {qu.dequeue()}")
		print(f"Deleted Item : {qu.dequeue()}")
		print(f"Deleted Item : {qu.dequeue()}")
		
		print("Queue Items :")
		qu.display()

	except Exception as e:
		print(e)
