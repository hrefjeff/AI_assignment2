#!/usr/bin/python

"""" Create DFS in python traversing a matrix using a stack """

matrixRowSize = 5
matrixColumnSize = 5

""" 
		Create Matrix
		-------------------------------
		| 0,0 | 1,0 | 2,0 | 3,0 | 4,0 |
		-------------------------------
		| 0,1 | 1,1 | 2,1 | 3,1 | 4,1 |
		-------------------------------
		| 0,2 | 1,2 | 2,2 | 3,2 | 4,2 |
		-------------------------------
		| 0,3 | 1,3 | 2,3 | 3,3 | 4,3 |
		-------------------------------
		| 0,4 | 1,4 | 2,4 | 3,4 | 4,4 |
		-------------------------------
"""

Matrix = [[0 for x in xrange(matrixRowSize)] for x in xrange(matrixColumnSize)]

for i in xrange(0,matrixRowSize):
	for j in xrange(0,matrixColumnSize):
		Matrix[i][j] = str(i) + str(j)
		print Matrix[i][j],
	print "\n"

# 1) Create a list T for candidates, and list V for visited

listT = []
listV = []

# 2) Initilize state

start = Matrix[0][2]
goal  = Matrix[1][0]

listT.append(start)


candidateNode = listT.pop()

print list(candidateNode[0])
print list(candidateNode[1])

# 3) Successor function

while candidateNode != goal:
	
	# Convert string coordinates to ints
	xCoordinate = list(candidateNode[0])
	intX = [ int(x) for x in xCoordinate ]
	yCoordinate = list(candidateNode[1])
	intY = [ int(x) for x in yCoordinate ]

	print Matrix[0][2]
	print Matrix[intX][intY]

# 	push N (x,[y + 1])
	listT.append(Matrix[intX][intY + 1])
#	push E ([x + 1],y)
	listT.append(Matrix[intX + 1][intY])
#	push S (x,[y - 1])
#	push W ([x - 1],y)

# if node in

	print listT
	candidateNode = listT.pop() 

print listV