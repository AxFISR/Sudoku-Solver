
#Algorithm:
#A backtracking method ,inserting a solution and move forward 
#if the solution is not acceptable we recursively return back
#and insert a different solution

Sudoku= [
                    [3,0,0,8,0,0,0,0,1],
                    [0,0,0,0,0,2,0,0,0],
                    [0,4,1,5,0,0,8,3,0],
                    [0,2,0,0,0,1,0,0,0],
                    [8,5,0,4,0,3,0,1,7],
                    [0,0,0,7,0,0,0,2,0],
                    [0,8,5,0,0,9,7,4,0],
                    [0,0,0,1,0,0,0,0,0],
                    [9,0,0,0,0,7,0,0,6]
    ]


#finds the indexes of empty cell (a value of 0) returns it or false if not found
def FindEmptyCell():
    indexes=[]
    for i in range(9):
        for j in range(9):
            if Sudoku[i][j] == 0:
                indexes = [i,j]
                return indexes
    return False

#checking 3 condition for a valid number ,vertical ,horizontal and grid 
def AcceptableInsert(Num,i,j):
    for ROW in range(9):
        if Sudoku[ROW][j] ==Num:
            return False
    
    #checks if number exists in the column
    for COL in range(9):
        if Sudoku[i][COL] ==Num:
            return False
    
    #calculates the first index of col and row for current grid
    GridCol = int((j//3)*3)
    GridRow = int((i//3)*3)
    
    for k in range(3):
        for r in range(3):
            if Sudoku[GridRow + k][GridCol + r] == Num:
                return False
    
    #returns true if all conditions met
    return True

def SudokuSolve():
    #if there is no empty cells left we return true
    EmptyCells = FindEmptyCell()
    if EmptyCells == False:
        return True
    i = EmptyCells[0]
    j = EmptyCells[1]
    
    #inserts a number if acceptable
    for Number in range(1,10):
        if AcceptableInsert(Number,i,j):
            Sudoku[i][j]= Number
            
            #checking the next insert ,if no acceptable solution found , backtracks recursively
            if SudokuSolve():
                return True
            #resets the previous insert to 0
            else:
                Sudoku[i][j]=0
    
    #returning false if nothing from 1 to Size is possible for insertion
    return False
            
        
def PrintSudoku():
    
    for i in range(9):
        for j in range(9):
            print(Sudoku[i][j], end = " ")
        print()
        
def main():
    print("Your Sudoku:")
    PrintSudoku()
    if SudokuSolve() == True:
        print("Your Sudoku Solution:")
        PrintSudoku()
    else:
        print("There is no solution for the current sudoku board")
        
main()
