# pqueue.py : Program to implement priority queue using linked list.

class Node:
	def __init__(self, value, priority):
		self.info = value
		self.priority = priority
		link = None

class PQueue:
	def __init__(self):
		self.front = None

	def is_empty(self):
		return self.front == None

	def enqueue(self, data, priority):
		temp = Node(data, priority)

		# Queue is empty or element to be added has priority more than first element
		if self.is_empty() or priority < self.front.priority:
			temp.link = self.front
			self.front = temp
		else:
			p = self.front
			while p.link is not None and p.link.priority<=priority:
				p = p.link
			temp.link = p.link
			p.link = temp

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
		if not self.is_empty():
			print("Priority, Data Item")
			p = self.front
			while p is not None:
				print(f"{p.priority} {p.info}")
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
	pq = PQueue()

	try:
		pq.enqueue(20,2)
		pq.enqueue(10,1)
		pq.enqueue(50,4)
		pq.enqueue(30,3)
		print("Queue Items :")
		pq.display()

		print(f"Front Item : {pq.peek()}")
		print(f"Total Items : {pq.size()}")
		print(f"Deleted Item : {pq.dequeue()}")
		print("Queue Items :")
		pq.display()

		pq.enqueue(40,5)
		print("Queue Items :")
		pq.display()

		print(f"Deleted Item : {pq.dequeue()}")
		print(f"Deleted Item : {pq.dequeue()}")
		print(f"Deleted Item : {pq.dequeue()}")
		print(f"Deleted Item : {pq.dequeue()}")
		print("Queue Items :")
		pq.display()
	except Exception as e:
		print(e)
