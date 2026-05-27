# gcd.py : Program to find greatest common divisor of two numbers.

def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a%b)

if __name__ == '__main__':
	num1=35
	num2=21

	print(f"GCD = {gcd(num1, num2)}")
