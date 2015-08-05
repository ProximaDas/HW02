#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
def two_by_two():
	plus = '+'
	hyp = '-'
	bar = '|'
	space = ' '
	horizontal = plus + hyp*4 + plus + hyp*4 + plus
	vertical = bar + space*4 + bar + space*4 + bar
	for x in range(1,12):
		if x in (1,6,11):
			print horizontal
		else:
			print vertical
	
def four_by_four():
	plus = '+'
	hyp = '-'
	bar = '|'
	space = ' '
	horizontal = (plus + hyp*4 + plus + hyp*4 ) * 2 + plus
	vertical = (bar + space*4 + bar + space*4 ) * 2 + bar
	for x in range(1,23):
		if x in (1,6,11,17,22):
			print horizontal
		else:
			print vertical
		 	
			
# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    two_by_two()
    four_by_four()



if __name__ == "__main__":
    main()