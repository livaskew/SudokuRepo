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

a = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print( "\n +---+---+---+---+---+---+---+---+---+" )

[ print( " |", row[i], end='' ) if i != 8
	else print( " |", row[i], "|\n +---+---+---+---+---+---+---+---+---+" )
	for row in a for i in range (len(row) ) ]

 
