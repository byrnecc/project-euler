''' Project Euler problem 14



The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

longestChain = 0
biggestNum = 0

# We will create a dictionary with numbers and their collatz length. 
# This way we can save working out the length of every number.
# key is number, value is length.
collatz = {1:1}


print('\n\nCollatz Sequence\n\n')

# num is the starting number
for num in range(2,1000000):
	chain = 0 # no. of terms in the chain
	n = num
	while n > 0 :
		if not n in collatz: # Check we don't have a length for this number in the table	
			if n % 2 == 0: #n is even
				n /= 2
			else: # n is odd
				n = (3 * n) + 1
			chain += 1
		else: # We have the collatz length for this number in our dictionary
			chain += collatz.get(n)
			break # exit the while loop as we already know the collatz length for the rest of the numbers
	if not num in collatz: # update our dictionary with the collatz length for num
		collatz.update({num:chain})
	if chain > longestChain:
		biggestNum = num
		longestChain = chain

		
print('The largest starting number under 1 million with the longest chain is:', biggestNum, 'with a chain of', longestChain, 'terms')
exit