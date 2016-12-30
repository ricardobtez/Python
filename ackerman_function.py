# Author: Ricardo Benitez
# Exercise Ackerman function by the suggestion of the book Think Python by Allen Downey

def ack(m,n):
	if(not m):
		return n + 1
	elif(not n):
		return ack(m-1,1)
	else:
		return ack(m-1,ack(m,n-1))
print(ack(3,4))
