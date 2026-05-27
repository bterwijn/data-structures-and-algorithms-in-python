# factorial.py : Program to find the factorial of a number using recursion.

def factorial(n):
	if n==0:
		return 1
	return (n * factorial(n-1))

if __name__ == '__main__':
	num = 5

	if num < 0:
		print("No factorial for negative number")
	else:
		print(f"Factorial of {num} = {factorial(num)}")
