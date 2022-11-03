from webbrowser import get
from box import Box


class GameBoard(object):

    # Attributes:
        # board - contains the 9 x 9 grid board
        # emptySquares - number of empty squares
        # rowDictionary - key is the row number and the value is an array of values in that row
        # colDictionary - key is the col number and the value is an array of values in that column
        # boxDictionary - key is the box number and the value is an array of values in that box


    # Functions
        # Update Empty Squares
        # Place Box - adds a the new box into the board
        # Get Empty Squares
        # Print Board
        # Populate Dictionaries
        # Update Domain and Degrees (Combined)
            # Update Domains - update domains in row, col, and grid of newly placed box
                # Done
            # Update Degrees - update degrees in row, col, and grid of newly placed box
                # Done
        # Remove Box - remove the box from board and updates dictionaries / domains / degrees

    def __init__(self, board):

        # Board is now initialized with '-' instead of 0 
        # This is not true its actualt initialized with 0s
        # self.board = [[Box('-', i, j, possibleValues) for i in range(9)] for j in range(9)]

        # boxDictionary - key is the box number and the value is an array of values in that box
        self.boxDictionary = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        # rowDictionary - key is the row number and the value is an array of values in that row
        self.rowDictionary = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        # colDictionary - key is the col number and the value is an array of values in that column
        self.colDictionary = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        self.openSpaces = 9 * 9

        self.board = self.initBoard(board)
        # self.emptySquares = self.findEmptySquares()
    
    # oldBoard is 2d array of just values
    def initBoard(self, oldBoard):
        # possibleValues = [1,2,3,4,5,6,7,8,9]
        # if user sends an invalid board, return an empty board
        # if(len(oldBoard) != 9 or len(oldBoard[0] != 9)):
        #     return [[Box('-', i, j, self.possibleValues) for i in range(9)] for j in range(9)]
     
        # newBoard = [[Box('0', j, i, possibleValues) for i in range(9)] for j in range(9)]
        newBoard = [[Box('0', j, i) for i in range(9)] for j in range(9)]

        for row in range(9):
            for col in range(9):
                newBoard[row][col].setValue(oldBoard[row][col])
                self.openSpaces -= 1
                #has to add value to dictonaries if not 0
                if(oldBoard[row][col] != 0):
                    self.rowDictionary[row].append(oldBoard[row][col])
                    self.colDictionary[col].append(oldBoard[row][col])
                    self.boxDictionary[newBoard[row][col].locBox].append(oldBoard[row][col])
                    # newBoard[row][col].possibleValues = [oldBoard[row][col]]
                
        #after all values have been set to the dictonaries go through a find possible values for each block
        # for row in range(9):
        #     for col in range(9):
        #         if(newBoard[row][col].value == 0):
        #              self.getPossibleValues(newBoard[row][col])

        # Update Domains
        # Update Degrees

        return newBoard

    # This function only applies after a new move is made
    # Function updates the domains of the corresponding row, col, and grid to the passed box
        # Also updates the degrees of the corresponding row, col, and grid
    def updateDomainsAndDegrees(self, box: Box):
        boxRow = box.locRow
        boxCol = box.locCol
        boxGrid = box.locGrid
        boxVal = box.value
        boxDegree = 0
        failure = False

        # Update Domains and Degrees for row of box
            # Find empty boxes in the row
            # Check if their domains contain the value of the placed box
            # If so, remove that value from their domains
        for i in range(0,9):
            # Check if box is empty and box domain contains the specified value
            if self.board[boxRow][i].value == 0 and boxVal in self.board[boxRow][i].domain:
                self.board[boxRow][i].domain.remove(boxVal)
                # Check if indexed box is in the same grid as main box
                # If it is, dont incremement the boxDegree
                # This ensures that no boxes are repeated
                # Also updates the degree of indexed box
                if self.board[boxRow][i].locGrid != boxGrid:
                    self.board[boxRow][i].degree -= 1
                    boxDegree += 1
                # Check if the change has removed all elements of the domain
                if len(self.board[boxRow][i].domain) == 0:
                    failure = True
                    break
        
        # Update Domains for col of box
        # Refer to Row Example for clarity
        if failure == False:
            for i in range(0,9):
                if self.board[i][boxCol].value == 0 and boxVal in self.board[i][boxCol].domain:
                    self.board[i][boxCol].domain.remove(boxVal)
                    if self.board[i][boxCol].locGrid != boxGrid:
                        self.board[i][boxCol].degree -= 1
                        boxDegree += 1
                    if len(self.board[i][boxCol].domain) == 0:
                        failure = True
                        break

        # Update Domains for grid of box
        if failure == False:
            gridRange = box.getGridRange()
            for i in range(gridRange[0], gridRange[1]+1):
                for j in range(gridRange[2], gridRange[3]+1):
                    if self.board[i][j].value == 0 and boxVal in self.board[i][j].domain:
                        self.board[i][j].domain.remove(boxVal)
                        # Incremement box degree for every value in the grid
                        boxDegree += 1
                        self.board[i][j].degree -= 1
                        if len(self.board[i][j].domain) == 0:
                            failure = True
                            break
        
        # Check if any Domain updates failed
        if failure == True:
            return None
        else:
            box.degree = boxDegree
        
        # Returns the box that was passed to it
        # This could be changed to return true or false as to whether it passed or not
        return box


    def isLegalValue(self, box: Box, value):
        allValues = set([1,2,3,4,5,6,7,8,9])
        notPossibleValues = set(self.boxDictionary[box.locBox] + (self.rowDictionary[box.locRow]) + (self.colDictionary[box.locCol]))
        # print(notPossibleValues)
        possibleValues = (allValues - notPossibleValues).union(notPossibleValues - allValues)
        if value in possibleValues:
            return True
        else:
            return False

        # box.possibleValues = list(possibleValues)
        # box.possibleValues.sort()

    #should itterate left to right to break ties according to instructions
    def findEmptySquare(self):
        for row in range(9):
            for col in range(9):
                if(self.board[row][col].value == 0):
                    return self.board[row][col]
        return None
    
    def printBoard(self):
        for row in self.board:
            values = []
            for val in row:
                values.append(val.value)          
            print(values)


    #returns if it is legal or not to add the value
    def add(self, placement):
        if isLegalValue() == True: #needs to be fixed
            self[placement.row][placement.column] = placement.value
            return True
        else:
            return False

    def checkConsistency(self, placement):
        #check the value in the row/col/box is not in any of the dictionaries
        desiredBox = getBoxNumber(placement)

        if placement.value in self.rowDictionary[placement.row] or placement.value in self.colDictionary[placement.col] or placement.value in self.boxDictionary[desiredBox]:
            return False
        return True

def getBoxNumber(placement):
    if(placement.row < 3 and placement.col < 3):
        return 0
    if(placement.row < 3 and placement.col >= 3 and placement.col < 6):
        return 1
    if(placement.row < 3 and placement.col >= 6 and placement.col < 9):
        return 2
    if(placement.row >= 3 and placement.row < 6 and placement.col < 3):
        return 3
    if(placement.row >= 3 and placement.row < 6 and placement.col >= 3 and placement.col < 6):
        return 4
    if(placement.row >= 3 and placement.row < 6 and placement.col >= 6 and placement.col < 9):
        return 5
    if(placement.row >= 6 and placement.row < 9 and placement.col < 3):
        return 6
    if(placement.row >= 6 and placement.row < 9 and placement.col >= 3 and placement.col < 6):
        return 7
    if(placement.row >= 6 and placement.row < 9 and placement.col >= 6 and placement.col < 9):
        return 8