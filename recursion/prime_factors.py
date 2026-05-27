# prime_factors.py : Program to find the prime factors of a number.

def prime_factors(num):
	i=2

	if num == 1:
		return

	while num%i != 0:
		i = i+1

	print(f"{i} ", end='')
	prime_factors(num/i)

if __name__ == '__main__':
	num = 84

	print(f"Prime factors of {num} : ", end='')
	prime_factors(num)
	print()
