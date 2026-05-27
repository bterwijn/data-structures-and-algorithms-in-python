# polynomial.py : Program of Polynomial expression creation, addition and multiplication using linked list.

class Node:
	def __init__(self, coefficient, exponent):
		self.coeff = coefficient
		self.expo = exponent
		self.link = None 

class Polynomial:
	def __init__(self):
		self.start = None

	def is_empty(self):
		return (self.start == None)

	def display(self):
		if not self.is_empty():
			p = self.start
			
			while p is not None:
				print(p.coeff,end='')
				if p.expo == 1:
					print("x",end='')
				elif p.expo > 1:
					print(f"x^{p.expo}", end='')
				p = p.link
				if p is not None:
					print(" + ", end='')
			print()
		else:
			print("Zero polynomial")

	def insert(self, coefficient, exponent):
		temp = Node(coefficient, exponent)
		# List empty or exponent greater than first one
		if self.is_empty() or exponent > self.start.expo:
			temp.link = self.start
			self.start = temp
		else:
			p = self.start
			while p.link is not None and p.link.expo >= exponent:
				p = p.link
			temp.link = p.link
			p.link = temp
	
	# Required for addition of polynomials
	def insert_at_end(self, coefficient, exponent):
		temp = Node(coefficient,exponent)

		if self.is_empty():
			self.start = temp
		else:
			p = self.start
			while p.link is not None:
				p = p.link

			p.link = temp

	def addition(self, list, result_list):
		p1 = self.start
		p2 = list.start
		
		while p1 is not None and p2 is not None:
			if p1.expo > p2.expo:
				result_list.insert(p1.coeff, p1.expo)
				p1 = p1.link
			elif p2.expo > p1.expo:
				result_list.insert(p2.coeff, p2.expo)
				p2 = p2.link
			elif p1.expo == p2.expo:
				result_list.insert(p1.coeff+p2.coeff, p1.expo)
				p1 = p1.link
				p2 = p2.link

		# If poly2 is finished and elements left in poly1
		while p1 is not None:
			result_list.insert(p1.coeff, p1.expo)
			p1 = p1.link

		# If poly1 is finished and elements left in poly2
		while p2 is not None:
			result_list.insert(p2.coeff, p2.expo)
			p2 = p2.link
	
	def multiplication(self, list, result_list):
		p1 = self.start
		p2 = list.start
		p2Start = p2

		if p1 is None or p2 is None:
			print("Multiplied polynomial is zero polynomial")
		else:
			while p1 is not None:
				p2 = p2Start
				while p2 is not None:
					result_list.insert(p1.coeff*p2.coeff, p1.expo+p2.expo)
					p2 = p2.link	
				p1 = p1.link

if __name__ == '__main__':
	list1 = Polynomial()
	list2 = Polynomial()
	list3 = Polynomial()
	list4 = Polynomial()

	list1.insert(4,3)
	list1.insert(5,2)
	list1.insert(-3,1)

	print("Polynomial List1 :")
	list1.display()

	list2.insert(2,5)
	list2.insert(6,4)
	list2.insert(1,2)
	list2.insert(8,0)

	print("Polynomial List2 :")
	list2.display()

	# Polynomial addition
	list1.addition(list2, list3)

	print("After addition of list1 and list2 :")
	list3.display()

	# Polynomial multiplication
	list1.multiplication(list2, list4)

	print("After multiplication of list1 and list2 :")
	list4.display()
