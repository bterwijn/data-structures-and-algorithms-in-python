# deque.py : Program to implement deque using circular list.

class Deque:
	def __init__(self, size=5):
		self.MAX_SIZE = size
		self.queue_list = [None] * self.MAX_SIZE
		self.front = -1
		self.rear = -1
	
	def is_empty(self):
		return self.front == -1
	
	def is_full(self):
		return self.front==0 and self.rear==self.MAX_SIZE-1 or self.front==self.rear+1
	
	def insert_front_end(self, data):
		if self.is_full():
			print("Queue Overflow")
		else:
			if self.front == -1: # If queue is initially empty
				self.front = 0
				self.rear = 0
			elif self.front == 0:
				self.front = self.MAX_SIZE-1
			else:
				self.front = self.front-1

			self.queue_list[self.front] = data
	
	def insert_rear_end(self, data):
		if self.is_full():
			print("Queue Overflow")
		else:
			if self.front == -1: # If queue is initially empty
				self.front = 0
				self.rear = 0
			elif self.rear == self.MAX_SIZE-1: # rear is at last position of queue
				self.rear = 0
			else:
				self.rear += 1

			self.queue_list[self.rear] = data
	
	def delete_front_end(self):
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
				self.front += 1

		return ret_value;
	
	def delete_rear_end(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		else:
			ret_value = self.queue_list[self.rear]

			if self.front == self.rear: # queue has only one element
				self.front = -1
				self.rear = -1
			elif self.rear == 0:
				self.rear = self.MAX_SIZE-1
			else:
				self.rear -= 1;

		return ret_value
	
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
					print(self.queue_list[i]);
					i += 1
				
				i=0;
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
	dq = Deque()

	try:
		dq.insert_front_end(2)
		dq.insert_front_end(1)
		dq.insert_rear_end(3)
		dq.insert_rear_end(4)

		print("Queue Items :")
		dq.display()
		print(f"Total items : {dq.size()}")

		print(f"Deleted Item from front : {dq.delete_front_end()}")
		print(f"Deleted Item from Rear : {dq.delete_rear_end()}")
		print("Queue Items :")
		dq.display()

		dq.insert_front_end(5)
		dq.insert_front_end(6)

		print("Queue Items :")
		dq.display()

		dq.insert_rear_end(7)

		print(f"Deleted Item : {dq.delete_front_end()}")
		print(f"Deleted Item : {dq.delete_rear_end()}")
		print(f"Deleted Item : {dq.delete_front_end()}")
		print(f"Deleted Item : {dq.delete_rear_end()}")
		print(f"Deleted Item : {dq.delete_front_end()}")

		print("Queue Items :")
		dq.display()

	except Exception as e:
		print(e)
