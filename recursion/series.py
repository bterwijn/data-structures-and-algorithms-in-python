# series.py : Program to display and find out the sum of series.
# Series : 1 + 2 + 3 + 4 + 5 +.......

def rseries(n):
	if n == 0:
		return 0
	sum = n + rseries(n-1)
	print(f"{n} + ", end='')
	return sum

if __name__ == '__main__':
	num = 5
	print(f"\b\b= {rseries(num)}") # \b to erase last + sign
