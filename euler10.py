""" Project Euler problem 10




The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


"""

# This code implements Sieve of Eratosthenes to generate all prime numbers
# up to the specified limit.

# Our dictionary array of numbers, up to input limit.
ArrayNumbers = {}

# The sum of all the discovered prime numbers
VarPrimeSum = 0


# Intro message and ask user for number input.
print()
print('Prime Number Sum Utility')
print('------------------------')
print()
print('This will print the sum of all prime numbers,')
print('up to the specified integer.')

# Check if input is actually a whole number and exit if it isn't.
try: 
	VarNum = int(input('Enter a number:'))
except TypeError:
	exit('Sorry, please enter a whole number.')
print()


# Convert negative number to positive, to prevent any funny business.
if VarNum < 0:
	VarNum = VarNum * -1

# create an array of all numbers up to VarNum. Start at 2 (first prime number).
for i in range(2,VarNum+1):
	ArrayNumbers[i] = True

# Work through our array, setting all multiples of j to False
# We don't need to go higher than square root of VarNum
for j in range(2,int(VarNum**0.5)+1):
	if ArrayNumbers[j] == True:
		for k in range(j**2,VarNum+1,j):
			ArrayNumbers[k] = False

			
# Now add together all the array keys with value True
for m in range(2,len(ArrayNumbers)+1):
	if ArrayNumbers[m] == True:
		VarPrimeSum += m

		
print('\n\nSum of all prime numbers up to',VarNum,'is:',VarPrimeSum)
exit()