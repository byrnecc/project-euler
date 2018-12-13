'''
Project Euler problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

# Build a lookup array of the length of each digit in the singles column.
# We need to count 0 - 19 to account for the teens. 
lenSingles = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]

# Build a lookup array of the length of each digit in the tens column.
lenTens = [0,3,6,6,5,5,5,7,6,6]

varTotal = 11 # just add value for 'one thousand' now

# cycle through numbers up to 999
for i in range(1,1000):
    ones = int(i % 10) # get the ones column
    tens = int((i - ones) / 10) # get the tens column
    if tens > 9: # get the hundreds column
        x = tens % 10
        huns = int((tens - x ) / 10) # get the hundreds column
        tens = int(x)
        varTotal += lenSingles[huns] # look up the value of the hundreds digit
        varTotal += 7 # add 7 for 'hundred'
        # Check if we need to add 'and' eg one hundred and one
        if tens + ones > 0:
            varTotal += 3
    else: # less than 100
        huns = 0
    if tens == 1:
        varTotal += lenSingles[ones + 10] # teen numbers
    else:
        varTotal += lenSingles[ones] + lenTens[tens]
print(varTotal)