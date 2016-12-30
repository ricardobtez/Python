# Author: Ricardo Benitez
# Exercise suggested in the book Think Python by Allen Downney

def is_triangle(a,b,c):
	if (a > (b+c)) or (b > (a+c)) or (c > (a+b)):
		print("No")
	else:
		print("Yes")
def using_is_triangle():
	a = int(input("The first argument is:\n"))
	b = int(input("The second argument is:\n"))
	c = int(input("The third argument is:\n"))
	is_triangle(a,b,c)
using_is_triangle()
