class Box(object):

    # Attributes:
        # value - holds the value of the box
        # possibleValues - array of the possible values of the box

    # Functions
        # Get Remaining Possible Values
        # Get Degree

    def __init__(self, value, locRow, locCol):

        self.value = value
        self.locRow = locRow
        self.locCol = locCol
        #have to do math to figure this out
        self.locBox = self.setBoxNum()
        # self.possibleValues = possibleValues

    def setBoxNum(self):
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