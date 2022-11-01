from box import Box


class GameBoard(object):

    # Attributes:
        # board - contains the 9 x 9 grid board
        # emptySquares - number of empty squares
        # rowDictionary - key is the row number and the value is an array of values in that row
    rowDictionary = {
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
    colDictionary = {
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
        # boxDictionary - key is the box number and the value is an array of values in that box
    boxDictionary = {
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

    # Functions
        # Update Empty Squares
        # Place Move
        # Get Empty Squares
        # Print Board
        # Populate Dictionaries


    def __init__(self):

        # Board is now initialized with '-' instead of 0
        possibleValues = [1,2,3,4,5,6,7,8,9]
        self.board = [[Box('-', i, j, possibleValues) for i in range(9)] for j in range(9)]

        self.emptySquares = 81


    def printBoard(self):
        for row in self.board:
            values = []
            for val in row:
                values.append(val.value)          
            print(values)