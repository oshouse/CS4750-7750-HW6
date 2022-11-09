# Main File

# Imports
from turtle import back
from board import GameBoard
from box import Box

def main():
    print("before board 1")
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
        print("solved board1 Ryan")
        board1.printBoard()
    else: 
        print("Board1 not solvable")

    #board 2 is not solvable
    print("before board 2")
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
        print("solved board2")
        board2.printBoard()
    else: 
        print("board2 not solvable")

    print("before board 3")
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
        print("solved board3")
        board3.printBoard()
    else: 
        print("board3 not solvable")

def backTracking(board : GameBoard):

    if(board.openSpaces == 0):
        return True
    
    emptyBox : Box = board.findMove()
    possibleValues = emptyBox.domain.copy()
    #evaluates values 1 through 9
    for value in possibleValues:

        # calls forward checking inside placeMove to make sure its a valid move
        if(board.placeMove(emptyBox, value)):
            if(backTracking(board)):
                return True

        board.removeMove(emptyBox, value)

            #if does not return true means that backtracking failed
            #have to undo everything
    return False


main()