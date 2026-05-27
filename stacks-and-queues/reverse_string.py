# reverse_string.py : Program of reversing a string using stack.

def reverse_string(str):
	stack_list = []
	temp = ""
	
	for char in str:
		stack_list.append(char)

	for i in range(0,len(stack_list)):
		temp += stack_list.pop()

	return temp
	
if __name__ == '__main__':
	str = "algorithms"
	print(f"String is : {str}")

	print(f"Reversed string is : {reverse_string(str)}")
