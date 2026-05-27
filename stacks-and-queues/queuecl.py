# queuecl.py : Program to implement queue using circular linked list.

class Node:
	def __init__(self,value):
		self.info = value 
		self.link = None

class QueueCL:
	def __init__(self):
		self.rear = None

	def is_empty(self):
		return self.rear == None

	def enqueue(self, data):
		temp = Node(data)

		if self.is_empty(): # If queue is empty
			self.rear = temp
			temp.link = self.rear
		else:
			temp.link = self.rear.link
			self.rear.link = temp
			self.rear = temp

	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		if self.rear.link == self.rear: # If only one element
			ret_value = self.rear.info
			self.rear = None
		else:
			ret_value = self.rear.link.info
			self.rear.link = self.rear.link.link

		return ret_value

	def peek(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		return self.rear.link.info

	def display(self):
		if self.is_empty() is not True:
			p = self.rear.link
			
			print(p.info)
			p = p.link
			while p is not self.rear.link:
				print(p.info)
				p = p.link
		else:
			print("Queue is empty")

	def size(self):
		count = 0

		if self.is_empty() is not True:
			p = self.rear.link
			
			count += 1
			p = p.link
			while p is not self.rear.link:
				count += 1
				p = p.link

		return count

if __name__ == '__main__':
	qu = QueueCL()

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
