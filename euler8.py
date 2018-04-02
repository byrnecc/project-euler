""" Project Euler problem 8

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


"""


# Create our number as a string.
varString = '73167176531330624919225119674426574742355349194934'
varString += '96983520312774506326239578318016984801869478851843'
varString += '85861560789112949495459501737958331952853208805511'
varString += '12540698747158523863050715693290963295227443043557'
varString += '66896648950445244523161731856403098711121722383113'
varString += '62229893423380308135336276614282806444486645238749'
varString += '30358907296290491560440772390713810515859307960866'
varString += '70172427121883998797908792274921901699720888093776'
varString += '65727333001053367881220235421809751254540594752243'
varString += '52584907711670556013604839586446706324415722155397'
varString += '53697817977846174064955149290862569321978468622482'
varString += '83972241375657056057490261407972968652414535100474'
varString += '82166370484403199890008895243450658541227588666881'
varString += '16427171479924442928230863465674813919123162824586'
varString += '17866458359124566529476545682848912883142607690042'
varString += '24219022671055626321111109370544217506941658960408'
varString += '07198403850962455444362981230987879927244284909188'
varString += '84580156166097919133875499200524063689912560717606'
varString += '05886116467109405077541002256983155200055935729725'
varString += '71636269561882670428252483600823257530420752963450'

# we know it is 1000 digits long but just to be sure, save it as a variable
varStringLen = len(varString)

# the below will store our largest answer
varLargestProduct = 0

# in the loop below, we will check 13 digits starting from position i at each loop
# we need 13 digits, so stop the loop when we get to 12 less than the length of the string
# remembering that range command terminates at 1 less than max (thus 12 not 13)
for i in range(0,varStringLen-12):
	# Now we have 13 digits out of the 1000 digit number, work out the product of these digits.
	# initialise testProduct to 1
	varTestProduct = 1
	for j in range(i,i+13):
		varTestProduct = varTestProduct * int(varString[j])
	# after all 12 digits are multiplied, check if we've found a larger answer so far
	if varTestProduct > varLargestProduct:
		varLargestProduct = varTestProduct
		varLargestProductDigits = varString[i:i+13]

print('Largest 13 digit product is:', varLargestProduct)
print('This is the product of the digits:', varLargestProductDigits)
exit()