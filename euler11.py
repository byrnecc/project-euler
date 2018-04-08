""" Project Euler problem 11

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

NOTE: grid data is read from this file in the lines above - don't edit anything above this line!
"""


def checkProduct(num1, num2, num3, num4):
	""" This function checks if the product of 4 passed integers
	is higher than any product calculated so far.
	If so it will save the product and its factors.
	"""
	global highestProduct 
	global highnum1
	global highnum2
	global highnum3
	global highnum4
	try:
		if int(num1) * int(num2) * int(num3) * int(num4) > highestProduct:
			highestProduct = int(num1) * int(num2) * int(num3) * int(num4)
			highnum1 = int(num1)
			highnum2 = int(num2)
			highnum3 = int(num3)
			highnum4 = int(num4)
	except TypeError:
		print('TypeError: Grid data must be whole numbers only.')

		
# The below store the highest product seen so far, and its factors 
highestProduct = 0 
highnum1 = 0
highnum2 = 0
highnum3 = 0
highnum4 = 0
		
		
# We need to create a matrix with all the numbers.
# Below creates a 2 dimensional list object. 
# first index is y (height/line number), second is x (width/column number)
# Actually 20 lists of 20 items each.
# Null-indexed, so last object in each list is 19.
matrix = []

# We will read the matrix data from this file
matfile = open('euler11.py')
matfiledata = matfile.readlines()

for i in range(4,25):	# Matrix data starts on line 4, goes for 20 lines. 
	matrix.append(matfiledata[i].split())

matfile.close()	
matrix.pop(-1)	# Gets rid of the empty item at the end of the list.


# matrix now contains our grid data.

# Now we begin checking for products.
# We will iterate through each item in matrix, 
# checking right, down, diagonally up+right and down+right
# We don't need to check up or left as we will have already cycled through 
# in those directions.
# Also need to be mindful of the edges of the grid.

for y in range(0,len(matrix)):	# iterates through each line in the grid data.
	for x in range(0,len(matrix[0])):	# iterates through each character on the grid lines
		# Make sure we are not less than 4 numbers away from edge of grid
		if x < len(matrix[0]) - 3:
			# First, check 4 numbers to the right
			num1 = matrix[y][x]
			num2 = matrix[y][x+1]
			num3 = matrix[y][x+2]
			num4 = matrix[y][x+3]
			checkProduct(num1, num2, num3, num4)
			# Now check up+right diagonal
			# Make sure we are not less than 4 numbers away from top of grid
			if y > 2:
				num1 = matrix[y][x]
				num2 = matrix[y-1][x+1]
				num3 = matrix[y-2][x+2]
				num4 = matrix[y-3][x+3]
				checkProduct(num1, num2, num3, num4)
			# Now check down+right diagonal
			# Make sure we are not less than 4 numbers away from bottom of grid
			if y < len(matrix) - 3:
				num1 = matrix[y][x]
				num2 = matrix[y+1][x+1]
				num3 = matrix[y+2][x+2]
				num4 = matrix[y+3][x+3]
				checkProduct(num1, num2, num3, num4)
		# Now check 4 numbers down.
		if y < len(matrix) - 3:
			num1 = matrix[y][x]
			num2 = matrix[y+1][x]
			num3 = matrix[y+2][x]
			num4 = matrix[y+3][x]
			checkProduct(num1, num2, num3, num4)

			
print()
print('The highest product is:',highestProduct)
print("It's factors are:", highnum1,highnum2, highnum3, highnum4)

exit()