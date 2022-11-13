# Main File

# Imports
import time
from board import GameBoard
from box import Box

instanceCount = 0

def main():
    run = input("Pick an instance to run (1,2,3): ")
    if run == "1":
        timer1 = time.perf_counter()
        instanceOne()
        timer2 = time.perf_counter()
        print("Run Time:", "{:.4f}".format(timer2 - timer1), "seconds")
    elif run == "2":
        timer1 = time.perf_counter()
        instanceTwo()
        timer2 = time.perf_counter()
        print("Run Time:", "{:.4f}".format(timer2 - timer1), "seconds")
    elif run == "3":
        timer1 = time.perf_counter()
        instanceThree()
        timer2 = time.perf_counter()
        print("Run Time:", "{:.4f}".format(timer2 - timer1), "seconds")



def instanceOne():
    print("\n----- Initial Board 1 -----")
    board1 = GameBoard([[0,0,1,0,0,2,0,0,0],
                        [0,0,5,0,0,6,0,3,0],
                        [4,6,0,0,0,5,0,0,0],
                        [0,0,0,1,0,4,0,0,0],
                        [6,0,0,8,0,0,1,4,3],
                        [0,0,0,0,9,0,5,0,8],
                        [8,0,0,0,4,9,0,5,0],
                        [1,0,0,3,2,0,0,0,0],
                        [0,0,9,0,0,0,3,0,0]])
    board1.printBoard()
    if(backTracking(board1)):
        print("----- Solved Board 1 ------")
        board1.printBoard()
    else: 
        print("Board1 not solvable")

def instanceTwo():
    #board 2 is not solvable
    print("\n----- Initial Board 2 -----")
    board2 = GameBoard([[0,0,5,0,1,0,0,0,0],
                        [0,0,2,0,0,4,0,3,0],
                        [1,0,9,0,0,0,2,0,6],
                        [2,0,0,0,3,0,0,0,0],
                        [0,4,0,0,0,0,7,0,0],
                        [5,0,0,0,0,7,0,0,1],
                        [0,0,0,6,0,3,0,0,0],
                        [0,6,0,1,0,0,0,0,0],
                        [0,0,0,0,7,0,0,5,0]])
    board2.printBoard()
    if(backTracking(board2)):
        print("----- Solved Board 2 ------")
        board2.printBoard()
    else: 
        print("board2 not solvable")

def instanceThree():
    print("\n----- Initial Board 3 -----")
    board3 = GameBoard([[6,7,0,0,0,0,0,0,0],
                        [0,2,5,0,0,0,0,0,0],
                        [0,9,0,5,6,0,2,0,0],
                        [3,0,0,0,8,0,9,0,0],
                        [0,0,0,0,0,0,8,0,1],
                        [0,0,0,4,7,0,0,0,0],
                        [0,0,8,6,0,0,0,9,0],
                        [0,0,0,0,0,0,0,1,0],
                        [1,0,6,0,5,0,0,7,0]])
    board3.printBoard()
    if(backTracking(board3)):
        print("----- Solved Board 3 ------")
        board3.printBoard()
    else: 
        print("board3 not solvable")



# Backtracking Algorithm
def backTracking(board : GameBoard):
    global instanceCount

    if(board.openSpaces == 0):
        return True
    
    emptyBox : Box = board.findMove()
    possibleValues = emptyBox.domain.copy()

    if instanceCount < 4:
                print("\nAssignment:", str(instanceCount+1))
                print("Assignment-Row: " + str(emptyBox.locRow))
                print("Assignment-Col: " + str(emptyBox.locCol))
                print("Domain Size:", len(possibleValues))
                print("Degree:", emptyBox.degree)

    #evaluates values 1 through 9
    for value in possibleValues:

        # calls forward checking inside placeMove to make sure its a valid move
        if(board.placeMove(emptyBox, value)):
            if instanceCount < 4:
                print("Value: ", value)
                instanceCount += 1
            if(backTracking(board)):
                return True

        board.removeMove(emptyBox, value)

            #if does not return true means that backtracking failed
            #have to undo everything
    return False


main()