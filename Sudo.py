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

 import collections
 from collections import deque


#need to define the thing that searches for empty boxes, still working on this
def findZero (a,t):
    for row in range (9):
        for col in range (9):
            if (a [row] [col] == 0):
                 t [0]= row
                 t [1]= col
                 t [2]= int
                return True
    return False

#check row, will return t or f whether or not a value has be used in a row
def usedRow (a, row, num)
    for i in range(9):
        if (a [row] [i] == num):
            return True
    return False
#check col, will return t or f whether or not a value had been used in a col
def usedCol (a, col, num)
    for i in range(9):
        if (a [i][col] == num)
            return True
    return False

#check box, will return t or f whethor or not a vlaue has been used in a subbox
def usedBox (a, row, col, num)
    for i in range(3):
        for j in range(3):
            if (a [row+1][col+j] === num):
                return True
        return False


#need to define the thing that sets constraints for unique integers range(9) per row/col/subboxes
# and set integer and recursivly fill grid
def findFill(a):
    for i in range(9), a[0] != a[i+1]
    for j in range(9), a[0] != a[j+1]
#set up subboxes?

#need to define the thing that solves the sudoku, this is the MAIN PROGRAM

def rsolve
    t=[0,0, int]
#using findZero, check if there are empty things. if there are empty things, return true and keep going
    if (not(findZero(a,t))):
        return True;
#consider digits 1 to 9
    for t for row in range(9)
    for t for col in range(9)





#need to set up bool if grid is solved then true and if grid cannot be solved then false.

#this is what t is for def findZero the recursive solve function, it tracks which empty cell we are at
t.append[int, [i, j]]


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



print( "\n +---+---+---+---+---+---+---+---+---+" )

[ print( " |", row[i], end='' ) if i != 8
else print( " |", row[i], "|\n +---+---+---+---+---+---+---+---+---+" )
for row in a for i in range (len(row) ) ]

 
