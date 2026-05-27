# string3.py : Program to display the string in reverse order.

def rdisplay(s, index):
	if s[index:] == '':
		return

	rdisplay(s, index+1)
	print(s[index], end='')

if __name__ == '__main__':
	s = "Algorithms"

	print("String is : ", end='')
	rdisplay(s, 0)
	print()
