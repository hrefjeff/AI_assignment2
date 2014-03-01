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

start = str(Matrix[0][2])
goal  = str(Matrix[1][0])

listT.append(start)

listT.append(Matrix[0][0])
listT.index("00") # <--- returs index of given number (useful for visited list)

print listT[1]

# if node is goal
# 	done
# else
# 	expand node n
# 	push N (x,[y + 1])
#	push E ([x + 1],y)
#	push S (x,[y - 1])
#	push W ([x - 1],y)

# 3) Successor function

# if node in 

# 4) Goal check