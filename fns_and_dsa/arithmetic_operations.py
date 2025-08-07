def perform_operation(num1, num2, operation):
	if operation == +:
		result = num1 = num2
		return result
	elif operation == -:
		result = num1 - num2
		return result
	elif operation == *:
		result = num1 * num2
		return result
	elif operation == /:
		if num2 != 0:
			result = num1 / num2
			return result
		else:
			return 'Error 0 is not divisble'
	else:
		return 'wrong operation sign'
