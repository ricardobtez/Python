# Author: Ricardo Benitez
# As suggested by the book Think Python version 2.0.17 from Allen Downey

from math import sqrt
def square_root(a):
    x = a/2
    epsilon = 0.0000001
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            return y
        x = y
for x in range(1,9):
	own_result = square_root(x)
	python_result = sqrt(x)
	print(x, own_result, python_result, abs(own_result - python_result))