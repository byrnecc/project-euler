""" Project Euler problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Euclids formula:
#
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# Where m > n > 0
#
# For our solution, a + b + c = 1000

# set initial value of m and n^2
m = 21
n = 1

# varSum holds our sum of a + b + c, to check answer meets conditions
varSum = 0


# Loop thru values of n until it is one less than m
# and until a + b + c = 1000
while varSum != 1000:
	for n in range(n,m):
		# apply Euclid's formula
		a = (m ** 2) - (n ** 2)
		b = 2 * m * n
		c = (m ** 2) + (n ** 2)
		# Check if our results match conditions for answer
		# of if a+b+c is more than 1000.
		# in both cases exit this for loop
		varSum = a + b + c
		if varSum >= 1000:
			break
	# Increment m by 1 for next loop and reset n
	# if VarSum = 1000 the while loop will exit and our answer has been found.
	m += 1
	n = 1
	
	
# print out the answer
print(f'a = {a}, b = {b}, c = {c}, sum of a+b+c = {a+b+c}') 
print(f'product abc = {a*b*c}')


exit()