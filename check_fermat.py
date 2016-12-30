# Author: Ricardo Benitez
# Exercise Check Fermat from the book Think Python Form Allen Downey

import math
def check_fermat(a,b,c,n):
	if (math.pow(a,n) + math.pow(b,n) - math.pow(c,n)) == 0.0:
		if(n >= 2):
			print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work")
def using_check_fermat():
	a = input("Give me the first number:\n")
	a = int(a)
	b = input("Give me the second number:\n")
	b = int(b)
	c = input("Give me the third number:\n")
	c = int(c)
	n = input("Give me the power:\n")
	n = int(n)
	check_fermat(a,b,c,n)
using_check_fermat()
