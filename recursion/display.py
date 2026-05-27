# display.py : Program to display numbers 1 to n and n to 1

def display1(n):
	if n==0:
		return

	print(n)
	display1(n-1)

def display2(n):
	if n==0:
		return

	display2(n-1)
	print(n)

if __name__ == '__main__':
	num = 5

	print(f"{num} to 1 :")
	display1(num)

	print(f"1 to {num} :")
	display2(num)