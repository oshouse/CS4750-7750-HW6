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


# None = Failure
# Solution = array of assignments to the board
# assignments is an array of tuples consisting of (row, col, value) value being 1-9
# placement is a tuple consisting of (row, col, value) value being 1-9

def backtrack(board: GameBoard, assignments):
    if boardCompleted(board, assignments) == True:
        return assignments
    variable = selectUnassignedVariable(board, assignments)  #one possible possible assignments. Returns a tuple of (row, col)
    domainValues = orderDomainValues(board, assignments, variable) #orders the domain of the values for the row and col selected

    for value in domainValues:
        possibleNewAssignment = (variable.row, variable.col, value)
        if consistent(possibleNewAssignment, assignments, board) == True: #compares the value to the suggested assignments. Only continues if the proposed domain value(what might work) is consistent with the already "assigned" value
            assignments.append(possibleNewAssignment) #adds the suggested move to the proposed "assignments"
            inferences = inference(board, assignments, variable) #finds the possible openings with the proposed assignment
            if inferences != None: #if there are inferences, then continue. If there is a single inference that does not work, then inferences will be None (failure)
                board.addInferences(inferences) #add the inferences to the board (basically checking if the proposed value will end up working)
                result = backtrack(board, assignments) #backtrack on the new board with the placed inferences
                if result != None: #if there is a solution, return it
                    return result #result is an array of assignments to make on the board
                else: #otherwise, remove the inferences from the proposed value, so that we can try a new value in that slot
                    board.removeInferences(inferences) #if a choice leads to failure either by inference checking or the backtrack on the board with the proposed inferences,
            assignments.remove(possibleNewAssignment) #then there is failure, so we need to remove this items from the assignments
    return None #if at the end of the algorithm there is no return successful result, then it is a failure

#checks if every assignment so far is consistent with the proposed assignment
def consistent(placement, assignments, board: GameBoard):
    for assignment in assignments:
        if arcConsistent(placement, assignment) != True:
            return False
    if board.checkConsistency(placement) == False:
        return False
    return True

def arcConsistent(move1, move2):
    if move1.value == move2.value:
        if move1.row == move2.row or move1.col == move2.col or inSameBox(move1, move2) == True:
            return False
    return True

def inSameBox(move1, move2):
    rowCheck = False 
    rowDifference = move1.row - move2.row
    if rowDifference < 0:
        rowDifference * -1
    if rowDifference <=3:
        rowCheck = True

    colCheck = False 
    colDifference = move1.col - move2.col
    if colDifference < 0:
        colDifference * -1
    if colDifference <=3:
        colCheck = True

    if rowCheck == True and colCheck == True:
        return True
    else:
        return False


#def inference(board, assignments, variables) need clarification on what exactly is a inference/how to find them
#do we add every possible combination of a row/column/box into it? If theres a failure obviously it stops, but if it works then inferences will be a hugeee array
                

def backtrackingSearch(board: GameBoard):
    assignments = []
    return backtrack(board, assignments)

def solveBoard(board: GameBoard):
    assignments = backtrackingSearch(board)
    for placement in assignments:
        board.add(placement)


def boardCompleted(board: GameBoard, assignments):
    newBoard = GameBoard(board)
    for placement in assignments:
        consistent = newBoard.add(placement)
    if consistent == True and board.spacesOpen == 0:
        return True
    else:
        return False
        

main()