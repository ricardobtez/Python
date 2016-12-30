# Author: Ricardo Benitez
# Exercise 6.6 of Think Python version 2.0.17 by Allen Downey

def first(word):
	return word[0]
def last(word):
	return word[-1]
def middle(word):
	return word[1:-1]
def is_palindrome(word):
	length = len(word)
	palabra = word
	for x in range (0,int(length/2)):
		if(first(palabra)==last(palabra)):
			palabra = middle(palabra)
		else:
			return False
	return True
print(first("noon"))
print(last("noon"))
print(middle("noon"))
print(is_palindrome("redivider"))
