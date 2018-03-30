""" Project Euler problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

SumSq = 0 # Sum of the squares
SqSum = 0 # Square of the sum
a = 0	# holds current Square of i value


# i is the natural numbers
for i in range(1,101):
	a = (i ** 2)
	SumSq = SumSq + a
	#print(f'#{i:4}:{total - a:5} + {a:5} = {total:5}')
	SqSum = SqSum + i

SqSum = SqSum ** 2

print()	
print('Sum of the Squares: ', SumSq)
print('Square of the Sums: ', SqSum)
print()
print('The difference between these two numbers is:', SqSum - SumSq) 
	
exit()