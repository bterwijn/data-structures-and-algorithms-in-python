# divisibility11.py : Program to find a number is divisible from 11 or not.
# A number is divisible by 11 if and only if the difference of the sums of digits at odd positions and even positions 
# is either zero or divisible by 11.

def is_divisible_by11(n):
	s1=0
	s2=0

	if n == 0:
		return True

	if n < 10:
		return False

	while n > 0:
		s1 += n%10
		n //= 10

		s2 += n%10
		n //= 10

	diff = (s1-s2) if s1>s2 else (s2-s1)

	return is_divisible_by11(diff)

if __name__ == '__main__':
	num = 62938194

	print(f"{num} is divisible by 11 : {is_divisible_by11(num)}")
