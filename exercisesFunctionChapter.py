# Author: Ricardo Benitez
# Exercises suggested by Allen Downey in his book Think Python

def right_justified(s):
	print(' '*(70 - len(s)) + s)
def do_twice(foo,value):
	foo(value)
	foo(value)
def print_twice(s):
	print(s)
	print(s)
def do_four(foo,value):
	do_twice(foo,value)
	do_twice(foo,value)
def grid_square(width,heigth,cw,ch):
	up = "+" + cw*"-"
	empty = "|" + cw*" "
	for x in range(0,heigth):
		print(width*up + "+")
		for y in range(0,ch):
			print(width*empty + "|")
	print(width*up + "+")
def grid():
	grid_square(8,4,4,2)
#do_four(grid_half,"hello")
#right_justified('Hello')
#do_four(print_twice,"spam")
grid()
