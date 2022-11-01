from box import Box


class GameBoard(object):

    # Attributes:
        # board - contains the 9 x 9 grid board
        # emptySquares

    # Functions
        # Update Empty Squares
        # Place Move
        # Get Empty Squares
        # Print Board

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