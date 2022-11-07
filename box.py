class Box(object):

    # Attributes:
        # value - holds the value of the box
        # possibleValues - array of the possible values of the box
        # degree - number of other boxes that are constrained by current box
            # i.e number of empty boxes in its row, col, and 3x3 box

    # Functions
        # Get Remaining Possible Values
        # Get Degree
        # Get Domain
        # Set Degree
        # Set Domain
        # Get Grid Range

    #domain = [1, 2, 3, 4, 5, 6, 7, 8, 9] # This is the possible values for this box
    #degree = 20 # This is the number of constrains that this box holds on others

    def __init__(self, value, locRow, locCol):

        self.value = value
        self.locRow = locRow
        self.locCol = locCol
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.degree = 0
        #have to do math to figure this out
        self.setGridNum()

    def setGridNum(self):
        if(self.locRow < 3 and self.locCol < 3):
            self.locGrid = 0
        if(self.locRow < 3 and self.locCol >= 3 and self.locCol < 6):
            self.locGrid = 1
        if(self.locRow < 3 and self.locCol >= 6 and self.locCol < 9):
            self.locGrid = 2
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol < 3):
            self.locGrid = 3
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol >= 3 and self.locCol < 6):
            self.locGrid = 4
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol >= 6 and self.locCol < 9):
            self.locGrid = 5
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol < 3):
            self.locGrid = 6
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol >= 3 and self.locCol < 6):
            self.locGrid = 7
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol >= 6 and self.locCol < 9):
            self.locGrid = 8
        

    def setValue(self, value):
        self.value = value

    # Returns array containing range of its grid
    # [rowStart, rowEnd, colStart, colEnd]
    def getGridRange(self):
        range = []
        if self.locGrid == 0:
            range = [0, 2, 0, 2]
        elif self.locGrid == 1:
            range = [0, 2, 3, 5]
        elif self.locGrid == 2:
            range = [0, 2, 6, 8]
        elif self.locGrid == 3:
            range = [3, 5, 0, 2]
        elif self.locGrid == 4:
            range = [3, 5, 3, 5]
        elif self.locGrid == 5:
            range = [3, 5, 6, 8]
        elif self.locGrid == 6:
            range = [6, 8, 0, 2]
        elif self.locGrid == 7:
            range = [6, 8, 3, 5]
        elif self.locGrid == 8:
            range = [6, 8, 6, 8]

        return range

    def printBox(self):
        print("Box Val: " + str(self.value) + " Row: " + str(self.locRow) + 
            " Col: " + str(self.locCol) + " Grid: " + str(self.locGrid) +
            " Deg: " + str(self.degree) + " Domain:", self.domain)