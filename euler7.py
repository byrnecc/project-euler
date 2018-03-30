""" Project Euler problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


# Our list of prime numbers that we will build
# 2 is the first prime so pre-populate our list
listPrimes = [ 2 ]


# countPrimes is how many prime numbers have been found so far
countPrimes = 1

def checkPrime(VarInt):
	"""
	This function will return True if the passed integer is a prime number.
	"""
	# 1 and 2 are prime
	#if VarInt <= 2:
	#	return True;
	# Check number is even, therefore not prime  - saves a few calculations
	#if VarInt % 2 == 0:
	#	return False;
	# Now check if VarInt is divisible by iterating numbers, starting at 3
	# and going up by 2 - skips all even numbers.
	for j in range(3,VarInt,2):
		if VarInt % j == 0:
			return False;
	# if the for loop did not exit, then this is a prime number.		
	return True;

	
# Intro message and ask user for number input.
print()
print('Prime Number Generator')
print('----------------------')
print()
print('This will generate a list of prime numbers, up to the nth number specified.')
# Check if input is actually a whole number and exit if it isn't.
try: 
	VarNum = int(input('Enter a Number:'))
except TypeError:
	exit('Sorry, please enter a whole number.')
print()


# Convert negative number to positive, to prevent any funny business.
if VarNum < 0:
	VarNum = VarNum * -1

# i is our iterator for the loops below. Start at 3 (second prime).
# increment i by 2 as even numbers after 2 aren't prime
i = 3
while countPrimes < VarNum:
	if checkPrime(i) == True:
		listPrimes.append(i)
		countPrimes += 1
	i += 2

j = 0
# Print out our results in a nice neat way
for j in range(0,len(listPrimes)):
	print(f' #{j+1:3}:{listPrimes[j]:6},', end='')
	if (j + 1) % 5 == 0:
		print('\n')
		
print('\n\nThe number',listPrimes[-1],'is #',j+1,'in sequence of all prime numbers.')
exit()