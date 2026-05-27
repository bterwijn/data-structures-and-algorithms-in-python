# check_parentheses.py : Program to check that parentheses in expression are valid or not.

def match_parentheses(left_par, right_par):
	if left_par=='(' and right_par==')':
		return True

	if left_par=='{' and right_par=='}':
		return True

	if left_par=='[' and right_par==']':
		return True

	return False

def is_valid(expr):
	st = []	# list as stack

	for i in range(len(expr)):
		if expr[i]=='(' or expr[i]=='{' or expr[i]=='[':
			st.append(expr[i])

		if expr[i]==')' or expr[i]=='}' or expr[i]==']':
			if len(st)==0:
				print("Right parentheses are more than left parentheses")
				return False
			else:
				ch = st.pop()
				if match_parentheses(ch, expr[i]) is not True:
					print("Parentheses are : ")
					print(f"{ch} and {expr[i]}")
					return False

	if len(st)==0:
		print("Balanced Parentheses")
		return True
	else:
		print("Left parantheses are more than right parantheses")
		return False

if __name__ == '__main__':
	expression = "[A/(B-C)*D]"

	print(f"Expression is : {expression}")

	if is_valid(expression):
		print("Valid expression")
	else:
		print("Invalid expression")
