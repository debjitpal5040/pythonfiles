def areBracketsBalanced(expr):
	stack = []
	for char in expr:
		if char in ["(", "{", "["]:
			stack.append(char)
		else:
			# IF current character is not opening bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	# Check Empty Stack
	if stack:
		return False
	return True

expr = "(())()"
if areBracketsBalanced(expr):
	print("Balanced")
else:
	print("Not Balanced")

