# Author: Ricardo Benitez
# Exercise suggested in the book Think Python by Allen Downey

import math
def eval_loop():
	evaluated = "Nothing to Evaluate"
	while True:	
		inn = input(">")
		if(inn == "done"):
			print(evaluated)
			break
		evaluated = eval(inn)
		print(evaluated)

eval_loop()