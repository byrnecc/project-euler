"""Project Euler problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


IntNum = 600851475143	# Number to derive prime factors from; the dividend.
ListFactors = []	# List containing the prime factors

def lowest_divisor(num):
	"""This function takes an integer as input for the dividend. 
	It calculates the lowest whole number divisor of the passed dividend with 
	no remainder.	
	The first returned value is the divisor and the second is the quotient.
	If the returned divisor is the same as the input integer, and quotient is
	1, the input number is prime and has no lower divisor.
	"""
	try:
		# Check that we aren't trying to factorize small or negative numbers
		if num <= 2:
			return(int(num),1)
		# Loop through numbers, starting at 2, to find lowest divisor.
		for i in range(2,num + 1):
			if num % i == 0:
				return(int(i),int(num / i));
	except TypeError:
		print('TypeError: lowest_divisor function takes whole numbers only.')
		return(False)
		
		
# Get the prime divisors 	
j = IntNum
while True:
	k = lowest_divisor(j)
	ListFactors.append(k[0])
	if k[0] == j:	
		# if true the divisor is prime, 
		# and we can't divide it any more
		break
	# if divisor isn't prime, continue the loop using quotient from 
	# the result of lowest_divisors(j) 	
	j = k[1]
			

print('The prime factors of', IntNum, 'are:', ListFactors)
print ('The largest prime factor is:', max(ListFactors))
exit()