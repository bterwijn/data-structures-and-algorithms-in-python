# sum_of_digits.py : Program to display digits of a number and sum of digits of that number.

# Displays digits of an integer number and finds the sum of digits of that number
def sum_of_digits(n):
	if n//10 == 0: # if n is a single digit number
		print(f"{n%10}", end='')
		return n

	sum = n%10 + sum_of_digits(n//10)
	print(f"{n%10}", end='')

	return sum
	
# Finds the sum of digits of an integer
# def sum_of_digits(n):
	# if n//10 == 0: # if n is a single digit number
		# return n
	# return n%10 + sum_of_digits(n//10)

# Displays the digits of an integer
# def display(n):
	# if n//10 == 0:
		# print(f"{n}", end='')
		# return

	# print(f"{n%10}", end='')
	# display(n//10)

# Displays the digits of an integer
# def display(n):
	# if n//10 == 0:
		# print(f"{n}", end='')
		# return

	# display(n//10)
	# print(f"{n%10}", end='')

if __name__ == '__main__':
	num = 45329

	print("Digits = ", end='')
	# display(num)
	print(f"\nSum of digits = {sum_of_digits(num)}")
