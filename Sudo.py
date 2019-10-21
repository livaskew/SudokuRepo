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


#need to define the thing that solves the sudoku, and basically defines the grid
def solve(a):
	for i in range (9)
	for j in range (9)
#need to define the thing that searches for empty boxes, still working on this
def findZero (a,1):
	for row in range (9):
	for col in range (9):
#i dont understand this next line, revisit    
 if (a [row] [col] == 0):
 	1[0]= row
	1[1]= col
	return True
return False

#need to define the thing that sets constraints for unique integers range(9) per row 
def rowFind(a):
	for i in range(9), a[1] != a[i+1]

#need to define the thing that sets constraints for unique integers range(9) per col
def colFind(a):
	for j in range(9), a[j] != a[j+1]
#need to define the thing that sets constraints for unique integers range(9) for subboxes

#need to define elif statement for each that will remove integer if its not working. this is the backtracking piece

#need to set up bool if grid is solved then true and if grid cannot be solved then false.









 if i != 0 return True
	elif return False

#Ians liv.py

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

 
