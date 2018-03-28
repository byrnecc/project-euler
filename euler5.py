""" Project Euler problem 5
2520 is the smallest number that can be divided by each of the numbers from
 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
 numbers from 1 to 20?
"""


# Found will be set to true when we have found a suitable number
Found = False;

# i will be the numbers to check that meet the criteria
# we know that the answer must be at least 2520
# and must be a multiple of 20
i = 2520


while Found == False:
	# j iterates through values 3 to 19. We know that answer will be divisible by 1, 2 and 20
	# i divided by j must have no remainder on each loop to be a valid answer
	for j in range(3,20):
		if i % j != 0:
			# as soon as we have non-zero remainder, we can discard this value
			# of i and move onto next number
			break
		elif j == 19:
			# If j has got to 19 without breaking the above for loop,
			# we have found our answer. exit the for loop
			Found = True;
	if Found == True:
		# exit the while loop
		break
	else:
	# increment i by 20 and start the for loop again
		i += 20

# At this point we have found our answer so print it out to verify
print('\n\tThe answer is:', i,'\n\n')
for k in range(1,21):
    print('{a:6} divided by {b:3} is: {c:10.0f} - remainder: {d:3}'.format(a=i, b=k, c=i/k, d=i%k))

	
exit()