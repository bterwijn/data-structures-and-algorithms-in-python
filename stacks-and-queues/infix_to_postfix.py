# infix_to_postfix.py : Program to covert infix to postfix and evaluate the postfix expression.
# It will evaluate only single digit numbers.

def power(b, a):
	result = 1

	i = 1
	while i <= a:
		result *= b
		i += 1

	return result
	
def evaluate_postfix(postfix):
	temp = 0
	st = []	# list as stack

	for symbol in postfix:
		if ord(symbol)-ord('0') >= 0 and ord(symbol)-ord('0') <= 9:
			st.append(ord(symbol)-ord('0'))
		else:
			a = st.pop()
			b = st.pop()
		
			if symbol == '+':
				temp = b+a
			elif symbol == '-':
				temp = b-a
			elif symbol == '*':
				temp = b*a
			elif symbol == '/':
				temp = b//a
			elif symbol == '%':
				temp = b%a
			elif symbol == '^':
				temp = power(b, a)

			st.append(temp)

	return st.pop()
	
def precedence(symbol):
	if symbol == '(':
		return 0
	elif symbol in '+-':
		return 1
	elif symbol in '*/%':
		return 2
	elif symbol == '^':
		return 3
	else:
		return 0
	
def infix_to_postfix(infix):
	postfix = "";
	st = [] # list as stack

	for symbol in infix:
		if symbol == '(':
			st.append(symbol)
		elif symbol == ')':
			while st[len(st)-1] != '(':
				postfix += st.pop()
			st.pop();
		elif symbol in '+-*/%^':
			while len(st) != 0 and ( precedence(st[len(st)-1]) >= precedence(symbol) ):
				postfix += st.pop()
			st.append(symbol)
		else:
			postfix += symbol

	while len(st) != 0:
		postfix += st.pop()
	
	return postfix

if __name__ == '__main__':
	infix = "7+5*3^2/(9-2^2)+6*4"

	print(f"Infix expression is : {infix}")

	postfix = infix_to_postfix(infix)

	print("Postfix expression is :")
	print(postfix)

	print("Value of expression is :")
	print(evaluate_postfix(postfix))
