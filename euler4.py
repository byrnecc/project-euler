""" Project Euler problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



# i will be the largest number to calculate palindromes for.
# 3 digit numbers = 999
i = 999
# k keeps the initial value of i, while i iterates down
k = i
# largest keeps track of largest palindrome we've found
largest = 0

# This loop factors all numbers from i down to k/10.

while i > k/10:
	j = k
	while j >= i:
		testProduct = i * j
		if str(testProduct) == str(testProduct)[::-1] and testProduct > largest:
			largest = testProduct
			factora = i
			factorb = j
		j = j - 1
	i = i - 1

	
print('Larget palindromic product is',largest)
print('Factors are',factora,'and',factorb)	
	
exit()