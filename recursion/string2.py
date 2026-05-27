# string2.py : Program to display the string.

def display(s, index):
	if(s[index:] == ''):
		return

	print(s[index], end='')
	display(s, index+1)

if __name__ == '__main__':
	s = "Sonbhadra"

	print("String is : ", end='')
	display(s, 0)
	print()
