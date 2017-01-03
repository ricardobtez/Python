# Author: Ricardo Benitez
# As suggested in the book Think Python

def square_root(a):
    x = a/2
    epsilon = 0.0000001
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            print(x)
            break
        x = y
#square_root(38)
