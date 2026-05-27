# tr_factorial.py : Program to find the factorial of a number using tail recursion.

def tr_factorial1(n, result):
	if n == 0:
		return result

	return tr_factorial1(n-1, n*result)

def tr_factorial(n):
	return tr_factorial1(n, 1)

if __name__ == '__main__':
	num = 5

	if num < 0:
		print("No factorial for negative number")
	else:
		print(f"Factorial of {num} = {tr_factorial(num)}")
