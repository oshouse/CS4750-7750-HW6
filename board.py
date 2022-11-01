from webbrowser import get
from box import Box


class GameBoard(object):

    # Attributes:
        # board - contains the 9 x 9 grid board
        # emptySquares - number of empty squares
        # rowDictionary - key is the row number and the value is an array of values in that row
    # rowDictionary = {
    #     0: [],
    #     1: [],
    #     2: [],
    #     3: [],
    #     4: [],
    #     5: [],
    #     6: [],
    #     7: [],
    #     8: []
    # }
    #     # colDictionary - key is the col number and the value is an array of values in that column
    # colDictionary = {
    #     0: [],
    #     1: [],
    #     2: [],
    #     3: [],
    #     4: [],
    #     5: [],
    #     6: [],
    #     7: [],
    #     8: []
    # }
    #     # boxDictionary - key is the box number and the value is an array of values in that box
    # boxDictionary = {
    #     0: [],
    #     1: [],
    #     2: [],
    #     3: [],
    #     4: [],
    #     5: [],
    #     6: [],
    #     7: [],
    #     8: []
    # }

    # Functions
        # Update Empty Squares
        # Place Move
        # Get Empty Squares
        # Print Board
        # Populate Dictionaries


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

        self.board = self.initBoard(board)
        # self.emptySquares = self.findEmptySquares()
    

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

        return newBoard

    def isPossibleValue(self, box: Box, value):
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