# power_of_number.py : Program to find the exponentiation of a number 
# (a power n, example 2 power 3 = 8).

def power(a, n):
	if n == 0:
		return 1

	return a * power(a, n-1)

if __name__ == '__main__':
	a=2
	n=4
	print(f"{a} power {n} = {power(a, n)}")
