class Box(object):

    # Attributes:
        # value - holds the value of the box
        # possibleValues - array of the possible values of the box

    # Functions
        # Get Remaining Possible Values
        # Get Degree

    def __init__(self, value, locRow, locCol, possibleValues):

        self.value = value
        self.locRow = locRow
        self.locCol = locCol
        self.possibleValues = possibleValues