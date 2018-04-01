""" Project Euler problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Euclids formula:
# Where m > n > 0
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
#
# For our solution, a + b + c = 1000


# set up our integers m and n below
m = 20
n = 2

a = (m ** 2) - (n ** 2)
b = 2 * m * n
c = (m ** 2) + (n ** 2)

print(f'a = {a}, b = {b}, c = {c}, sum of a+b+c = {a+b+c}') 
print(f'product abc = {a*b*c}')


exit()