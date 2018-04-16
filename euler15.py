''' 
Project Euler problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''


# To reach the destination, we need to move s times down and s times right
# where s is side length of the square. i.e. 2s moves.
# How many different combinations of moves can we make?
#
# This problem can be solved with the Binomial Coefficient formula.
# Formula is:
# x! / (x-y)! * y!
# x is number of distinct terms, y is size of the subsets. 
# i.e. out of 2s possible moves how many different combos of s size can we make?


def factorial(n):
	''' Recursive function that calculates the value of n! '''
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		
		
print('\nLattice Paths\n')
print('This program calculates the possible routes through a square grid,')
print('starting at the top left and moving either right or down to reach')
print('the lower right corner.\n')

y = input('Enter the side length of your square grid:')
try:
	y = int(y) 
	x = y + y # our total number of moves (distinct terms) in a square lattice is double the side length (subset size)
except:
	print('Sorry, please enter a whole number.')
	exit(1)
	

x_factorial = factorial(x)
y_factorial = factorial(y)

paths = x_factorial / y_factorial ** 2 # in a square grid, x-y always equals y, so formula can be condensed to y! ** 2

print('Total number of possible routes through square grid of size',y,'is:',int(paths))