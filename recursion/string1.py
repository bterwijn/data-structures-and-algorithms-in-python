# string1.py : Program to find the length of a string.

def length(s, index):
	if(s[index:] == ''):
		return 0

	return 1 + length(s,index+1)

if __name__ == '__main__':
	s = "Lucknow"

	print(f"String is : {s}")
	print(f"Length : {length(s,0)}")