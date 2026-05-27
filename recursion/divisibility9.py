# divisibility9.py : Program to find a number is divisible from 9 or not.
# A number is divisible by 9 if and only if the sum of digits of the number is divisible by 9.

def is_divisible_by9(n):
	sum_of_digits = 0

	if n == 9:
		return True

	if n < 9:
		return False

	while n > 0:
		sum_of_digits += n%10
		n //= 10

	return is_divisible_by9(sum_of_digits)

if __name__ == '__main__':	
	num = 1469358

	print(f"{num} is divisible by 9 : {is_divisible_by9(num)}")
