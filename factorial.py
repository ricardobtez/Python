# Author: Ricardo Benitez
# Recursive factorial function

def factorial(n):
	if(not isinstance(n,int)) or (n<0):
		print("The function is only defined for positive integers")
		return None
	elif(not n):
		return 1
	else:
		return n * factorial(n-1)
print(factorial(4))
