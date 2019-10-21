#basic idea:

#https://www.geeksforgeeks.org/sudoku-backtracking-7/
# Find row, col of an unassigned cell
 # If there is none, return true
  #For digits from 1 to 9
   # a) If there is no conflict for digit at row, col
    #    assign digit to row, col and recursively try fill in rest of grid
   # b) If recursion successful, return true
  #  c) Else, remove digit and try another
 # If all digits have been tried and nothing worked, return false

#Ians liv.py


def solve(a):
	for i in range (9)
	for j in range (9)

def findZero (a,1):
	for row in range (9):
	for col in range (9):
#i dont understand this next line, revisit    
 if (a [row] [col] == 0):
 	1[0]= row
	1[1]= col
	return True
return False



 if i != 0 return True
	elif return False

a = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [ 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

solve (a)

print( "\n +---+---+---+---+---+---+---+---+---+" )

[ print( " |", row[i], end='' ) if i != 8
	else print( " |", row[i], "|\n +---+---+---+---+---+---+---+---+---+" )
	for row in a for i in range (len(row) ) ]

 
