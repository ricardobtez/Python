# Author: Ricardo Benitez
# Recursive fibbonacci series

def fibbonacci(n):
	if(not n):
		return 0
	elif(n==1):
		return 1
	else:
		return fibbonacci(n-1) + fibbonacci(n-2)
print(fibbonacci(3))