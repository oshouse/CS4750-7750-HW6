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
        print("solved board1")
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

    emptyBox = board.findEmptySquare()
    if(emptyBox == None):
        return True

    #evaluates values 1 through 9
    for value in range(1, 10):

        if(board.isPossibleValue(emptyBox, value)):
            board.board[emptyBox.locRow][emptyBox.locCol].value = value

            board.rowDictionary[emptyBox.locRow].append(value)
            board.colDictionary[emptyBox.locCol].append(value)
            board.boxDictionary[emptyBox.locBox].append(value)

            if(backTracking(board)):
                return True
            
            #if does not return true means that backtracking failed
            #have to undo everything

            board.board[emptyBox.locRow][emptyBox.locCol].value = 0
            board.rowDictionary[emptyBox.locRow].remove(value)
            board.colDictionary[emptyBox.locCol].remove(value)
            board.boxDictionary[emptyBox.locBox].remove(value)

    return False
        

main()