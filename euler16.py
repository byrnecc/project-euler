'''
Project Euler problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

# Var to hold our answer
numsum = 0

# Calculate the number. Get the length i.e. number of digits
num = 2**1000
numstr = str(num)
numlen = len(numstr)

print(numstr[0])
# Cycle though each digit in numstr and add it to the total.
for i in range(0,numlen):
    numsum += int(numstr[i])

print("The answer is:",numsum)