#
# Project Euler problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
#
# First define our range of numbers to loop through
varTotal=0
for num in range(0,1000):
	# check if divisible by 3 or 5
	if num % 3 == 0 or num % 5 == 0:
	# if true add to our running total
		varTotal += num
		print(num, 'is divisible by 3 or 5! adding to total')
		print('Total is now:',varTotal)
#at completion of loop, print the running total	
print('Grand total is:', varTotal)
exit()	