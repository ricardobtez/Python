# Author: Ricardo Benitez
# Exercise suggested in the book Think Python by Allen Downey

from math import sqrt
from math import pow
from math import pi
def factorial(n):
	if(not isinstance(n,int)) or (n<0):
		print("The function is only defined for positive integers")
		return None
	elif(not n):
		return 1
	else:
		return n * factorial(n-1)

def estimate_pi():
	constant = (2 * sqrt(2)) / 9801
	addition = 0.0
	division = 1.0
	epsilon = 1e-15
	k = 0
	while division > epsilon:
		numerator = factorial(4*k) * (1103 + 26390*k)
		denominator = factorial(k)**4 * 296**(4*k)
		k = k + 1
		division = numerator / denominator
		addition = addition + division
	approximate = constant * addition
	approximate = 1 / approximate
	return approximate

print(estimate_pi())
print(pi)
print("The difference is:" , abs(estimate_pi() - pi))