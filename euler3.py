# 
# Project Euler problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

varNum = 13195	# Number to derive prime factors from; the dividend.

def lowest_denominator( num ):
	"Function returns the lowest whole number divisor of the passed dividend, with no remainder."
	# Loop through numbers, starting at 2, to find lowest denominator
	for i in range(2,99):
		if num % i == 0:
			return(int(i));
			
print(lowest_denominator(13195))

exit()