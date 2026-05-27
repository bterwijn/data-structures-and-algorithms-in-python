# base_conversion.py : Program to convert a positive decimal number to Binary, Octal or Hexadecimal.

def convert_base(num, base):
	rem = num%base

	if num==0:
		return

	convert_base(num//base, base)

	if rem < 10:
		print(f"{rem}", end='')
	else:
		print(f"{chr(rem-10+ord('A'))}", end='')

if __name__ == '__main__':
	num = 20

	print(f"Binary : ", end='')
	convert_base(num, 2)
	print()
	print(f"Octal : ", end='')
	convert_base(num, 8)
	print()
	print(f"Hexadecimal : ", end='')
	convert_base(num, 16)
	print()
