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


# need to define the thing that searches for empty boxes, still working on this
def findZero (a,t):
    for row in range (9):
        for col in range (9):
            if (a [row] [col] == 0):
                t[0]= row
                t[1]= col
            return True
    return False

# check row, will return t or f whether or not a value has be used in a row


def usedRow(a, row, n):
    for i in range(9):
        if (a [row] [i] == n):
            return True
    return False
# check col, will return t or f whether or not a value had been used in a col


def usedCol (a, col, n):
    for i in range(9):
        if (a [i][col] == n):
            return True
    return False

# check box, will return t or f whethor or not a vlaue has been used in a subbox


def usedBox (a, row, col, n):
    for i in range(3):
        for j in range(3):
            if (a [row+1][col+j] == n):
                return True
        return False
# check to see if the move is ok, we call this legal


def legal(a, row, col, n):
    return not usedRow(a, row, n) and not usedCol(a, col, n) and not usedBox(a, row-row%3, col-col%3, n)

# and set integer and recursively fill grid (kinda recursive, but not in the way we learned).


def findFill(a):
    t=[0,0]
    if (not findZero(a,t)):
        return True
    row=t[0]
    col=t[1]
    for n in range (1, 10, 1):
        if(legal(a, row, col, n)):
            a[row][col]= n
            if findFill(a):
                return True
            a[row][col]= 0
    return False


# need to define the thing that solves the sudoku, this is the MAIN PROGRAM
if __name__ == "__main__":

    a = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (findFill(a)):
    print("\n +---+---+---+---+---+---+---+---+---+")
    [print(" |", row[i], end='') if i != 8
        else print(" |", row[i], "|\n +---+---+---+---+---+---+---+---+---+")
            for row in a for i in range (len(row) )]




 
