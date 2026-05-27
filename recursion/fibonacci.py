# fibonacci.py : Program to generate fibonacci series.

def fib(n):
	if n==0 or n==1:
		return 1

	return (fib(n-1) + fib(n-2))

if __name__ == '__main__':
	nterms = 10

	for i in range(nterms):
		print(f"{fib(i)} ", end='')

	print()
