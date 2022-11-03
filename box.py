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

    def __init__(self, value, locRow, locCol):

        self.value = value
        self.locRow = locRow
        self.locCol = locCol
        #have to do math to figure this out
        self.locGrid = self.setBoxNum()
        # self.domain = domain # This is the possible values for this box

    def setGridNum(self):
        if(self.locRow < 3 and self.locCol < 3):
            return 0
        if(self.locRow < 3 and self.locCol >= 3 and self.locCol < 6):
            return 1
        if(self.locRow < 3 and self.locCol >= 6 and self.locCol < 9):
            return 2
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol < 3):
            return 3
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol >= 3 and self.locCol < 6):
            return 4
        if(self.locRow >= 3 and self.locRow < 6 and self.locCol >= 6 and self.locCol < 9):
            return 5
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol < 3):
            return 6
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol >= 3 and self.locCol < 6):
            return 7
        if(self.locRow >= 6 and self.locRow < 9 and self.locCol >= 6 and self.locCol < 9):
            return 8
        

    def setValue(self, value):
        self.value = value