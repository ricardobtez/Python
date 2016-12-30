# Author: Ricardo Benitez
# Exercise 6.7 of Think Python version 2.0.17 by Allen Downey

def is_power(a,b):
	quotient = a/b
	remainder = a%b
	if((not remainder) and (quotient == 1.0)):
		return True
	elif (not remainder) and quotient != 1.0:
		return is_power(quotient,b)
	else:
		return False

print(is_power(36,6))`