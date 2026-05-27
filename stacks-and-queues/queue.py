# queue.py : Program to implement queue using list.

class Queue:
	def __init__(self, size=5):
		self.MAX_SIZE = size
		self.queue_list = [None] * self.MAX_SIZE
		self.front = -1
		self.rear = -1

	def is_empty(self):
		return self.front==-1 or self.front==self.rear+1

	def is_full(self):
		return self.rear == self.MAX_SIZE-1
	
	def enqueue(self, data):
		if self.is_full():
			print("Queue Overflow")
		else:
			if self.front == -1:
				self.front = 0

			self.rear += 1
			self.queue_list[self.rear] = data
	
	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		ret_value = self.queue_list[self.front]
		self.front += 1
		return ret_value
	
	def peek(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		return self.queue_list[self.front]
	
	def display(self):
		print(f"Front = {self.front}	rear = {self.rear}")

		if self.is_empty():
			print("Queue is empty")
		else:
			i = self.front
			while i <= self.rear:
				print(self.queue_list[i])
				i += 1

	def size(self):
		ret_value = 0

		if self.is_empty() is not True:
			ret_value = self.rear-self.front+1

		return ret_value

if __name__ == '__main__':
	qu = Queue()

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
