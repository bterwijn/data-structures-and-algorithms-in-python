# summation.py : Program to find summation of numbers from 1 to n

def summation(n):
	if n==0:
		return 0
	return n + summation(n-1)

if __name__ == '__main__':
	num = 5
	print(f"Summation({num}) = {summation(num)}")
