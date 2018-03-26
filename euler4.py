""" Project Euler problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# i will be the largest number to calculate palindromes for.
# 3 digit numbers = 999
i = 999
# k keeps the initial value of i, while i iterates down
k = i
# found is set to True when the palindrome is found, to break both while loops
found = False


# This loop factors all numbers from i down to k/10.
while i > (k/10):
	j = i
	while j > (k/10):
		testProduct = i * j
		# Find out if testProduct is even or odd, to account for middle digit.
		# First get the first half of the number into PalFront
		# Then get the second half of the number into PalRear
		palCheck = str(testProduct)
		testLen = len(palCheck)
		if testLen % 2 == 0:
			testLenHalf = int(testLen / 2)
			palFront = palCheck[0:int(testLenHalf)]
			palRear = palCheck[-1:testLenHalf-1:-1]
		else:
			testLenHalf = int((testLen - 1) / 2)
			palFront = palCheck[0:testLenHalf]
			palRear = palCheck[-1:testLenHalf:-1]
		# check for palindromic numbers 
		if palFront == palRear:
			print('Larget palindromic product is',testProduct)
			print('Factors are',i,'and',j)
			found = True
			break
		j = j - 1
	if found == True:
		break
	i = i - 1
exit()