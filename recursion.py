# Author: Allen Downey
# From the book Think Python by Allen Downey

def countdown(n):
	if n <= 0:
		print("finished")
	else:
		print(n)
		countdown(n-1)

countdown(-1)
