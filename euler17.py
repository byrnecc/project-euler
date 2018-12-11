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
lenSingles = list(4,3,3,4,4,3,5,5,4,3,6,6,8,8,7,7,8,8)

# Build a lookup array of the length of each digit in the tens column.
# 0 and 1 have no length, as the latter is included in the singles/teens
lenTens = list(0,0,6,6,5,5,5,6,6)

# Build a lookup array of the length of each digit in the hundreds column.
# Need to add 3 for 'and' eg two hundred and eleven...
lenHundreds = list(0,13,13,15,14,14,13,15,15,14)

# Lookup array for thousands column - either 0 (for <1000) or 13 (for =1000)
lenThousands = list(0,11)