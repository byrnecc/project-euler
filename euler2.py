# Project Euler problem 2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# Define variables
varTotal=0	# running total
varOldNo=1	# first number to be added to make the fibonacci number. preset to 1 to start the sequence
varOlderNo=0	# second number to be added to make the fibonacci number.
varFibNo=0	# current fibonacci number. sum of varOldNo and VarOlderNo

# main loop through all numbers

while True:
	# Add the two old numbers together to get the next in sequence
	varFibNo = varOldNo + varOlderNo
	# check we are still under 4 million
	if varFibNo > 4000000:
		break
	# rotate the old numbers, will add them together on next loop
	varOlderNo = varOldNo
	varOldNo = varFibNo
	# check if this number is even-valued
	if varFibNo % 2 == 0:
	# add even number to our running total
		varTotal += varFibNo
		print(varFibNo, 'is an even Fibonacci sequence number, adding to total.')

#at completion of loop, print the running total	
print('Total:',varTotal)
exit()	