# cqueue.py : Program to implement circular queue using list.

class CQueue:
	def __init__(self, size=5):
		self.MAX_SIZE = size
		self.queue_list = [None] * self.MAX_SIZE
		self.front = -1
		self.rear = -1

	def is_empty(self):
		return self.front == -1

	def is_full(self):
		return self.front==0 and self.rear==self.MAX_SIZE-1 or self.front==self.rear+1
	
	def enqueue(self, num):
		if self.is_full():
			print("Queue Overflow")
		else:
			if self.front == -1:
				self.front = 0

			if self.rear == self.MAX_SIZE-1: # rear is at last position of queue
				self.rear = 0
			else:
				self.rear = self.rear+1

			self.queue_list[self.rear] = num
	
	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		else:
			ret_value = self.queue_list[self.front]

			if self.front == self.rear: # queue has only one element
				self.front = -1
				self.rear = -1
			elif self.front == self.MAX_SIZE-1:
				self.front = 0
			else:
				self.front = self.front+1

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
			if self.front <= self.rear:
				while i <= self.rear:
					print(self.queue_list[i])
					i += 1
			else:
				while i <= self.MAX_SIZE-1:
					print(self.queue_list[i])
					i += 1
				
				i=0
				while i <= self.rear:
					print(self.queue_list[i])
					i += 1
	
	def size(self):
		if self.is_empty():
			return 0

		if self.is_full():
			return self.MAX_SIZE-1

		i = self.front
		sz = 0

		if self.front <= self.rear:
			while i <= self.rear:
				sz += 1
				i += 1
		else:
			while i <= self.MAX_SIZE-1:
				sz += 1
				i += 1

			i = 0
			while i <= self.rear:
				sz += 1
				i += 1

		return sz

if __name__ == '__main__':
	cq = CQueue()

	try:
		cq.enqueue(1)
		cq.enqueue(2)
		cq.enqueue(3)
		cq.enqueue(4)

		print("Queue Items :")
		cq.display()
		print(f"Front Item : {cq.peek()}")
		print(f"Total items : {cq.size()}")

		print(f"Deleted Item : {cq.dequeue()}")
		print(f"Deleted Item : {cq.dequeue()}")
		print("Queue Items :")
		cq.display()

		cq.enqueue(5)
		cq.enqueue(6)

		print("Queue Items :")
		cq.display()

		cq.enqueue(7)

		print(f"Deleted Item : {cq.dequeue()}")
		print(f"Deleted Item : {cq.dequeue()}")
		print(f"Deleted Item : {cq.dequeue()}")
		print(f"Deleted Item : {cq.dequeue()}")
		print(f"Deleted Item : {cq.dequeue()}")
		
		print("Queue Items :")
		cq.display()

	except Exception as e:
		print(e)
