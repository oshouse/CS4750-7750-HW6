# Board Class

# Imports
from box import Box

class GameBoard(object):

    # Attributes:
        # board - contains the 9 x 9 grid board
        # openSpaces - number of open spaces
        # rowDictionary - key is the row number and the value is an array of values in that row
        # colDictionary - key is the col number and the value is an array of values in that column
        # gridDictionary - key is the grid number and the value is an array of values in that box


    # Functions
        # Update Open Spaces
        # Place Move - adds a the new box into the board - sets value in box, updates dictionaries, and updates domains and degrees
        # Find Move - uses mrv, degree heuristics, and tiebreaking to find next best move
        # Get Open Spaces
        # Set Open Spaces
        # Print Board
        # Populate Dictionaries
        # Set Domain - Initialize domain for each box 
        # Set Degree = Initialize degree for each box
        # Update Domain and Degrees (Combined) 
            # Update Domains - update domains in row, col, and grid of newly placed box
            # Update Degrees - update degrees in row, col, and grid of newly placed box
        # Remove Box - remove the box from board and updates dictionaries / domains / degrees
        # Get Highest Degree - get boxes with highest degree value
        # Get Lowest Domain - get boxes with smallest domain

    def __init__(self, board):

        # gridDictionary - key is the box number and the value is an array of values in that box
        self.gridDictionary = {
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
        self.board = [[Box('0', 0, 0) for i in range(9)] for j in range(9)]
        for row in range(9):
            for col in range(9):
                self.board[row][col].setValue(board[row][col])
                self.board[row][col].locRow = row
                self.board[row][col].locCol = col
                self.board[row][col].setGridNum()

                if(board[row][col] != 0):
                    self.openSpaces -= 1
                    self.rowDictionary[row].append(board[row][col])
                    self.colDictionary[col].append(board[row][col])
                    self.gridDictionary[self.board[row][col].locGrid].append(board[row][col])

        # Set the domains and degrees based on starting board
        for row in range(9):
            for col in range(9):
                self.setDomains(row, col)
                
        for row in range(9):
            for col in range(9):
                self.setDegrees(row, col)

    def setOpenSpaces(self, openSpaces):
        self.openSpaces = openSpaces

    # Sets the domain of the box at the row and col
    def setDomains(self, row, col):
        if self.board[row][col].value == 0:
            # subtract values in rowDictionary from domain
            for val in self.rowDictionary[self.board[row][col].locRow]:
                if val in self.board[row][col].domain:
                    self.board[row][col].domain.remove(val)

            for val in self.colDictionary[self.board[row][col].locCol]:
                if val in self.board[row][col].domain:
                    self.board[row][col].domain.remove(val)

            for val in self.gridDictionary[self.board[row][col].locGrid]:
                if val in self.board[row][col].domain:
                    self.board[row][col].domain.remove(val)
        else:
            self.board[row][col].domain.clear()

    # Sets the degrees of the box at the row and col
    # Degree in each empty box is based on if their own domain correlates with indexed box domain
    def setDegrees(self, row, col):
        if self.board[row][col].value == 0:
            # Check row and col
            for i in range(9):
                # Reset row and col booleans
                rowFound = False
                colFound = False
                # Loop through all values in domain
                for val in self.board[row][col].domain:
                    # If value in row is empty, value in main box domain is in indexed box domain, and specific box hasn't been found
                    if self.board[row][i].value == 0 and val in self.board[row][i].domain and not rowFound and i != col:
                        if self.board[row][i].locGrid != self.board[row][col].locGrid:
                            rowFound = True
                            self.board[row][col].degree += 1
                    # If value in col is empty, value in main box domain is in indexed box domain, and specific box hasn't been found
                    if self.board[i][col].value == 0 and val in self.board[i][col].domain and not colFound and i != row:
                        if self.board[i][col].locGrid != self.board[row][col].locGrid:
                            colFound = True
                            self.board[row][col].degree += 1
            # Check grid
            gridRange = self.board[row][col].getGridRange()
            for i in range(gridRange[0], gridRange[1]+1):
                for j in range(gridRange[2], gridRange[3]+1):
                    for val in self.board[row][col].domain:
                        if self.board[i][j].value == 0 and val in self.board[i][j].domain and (i != row or j != col):
                            self.board[row][col].degree += 1
                            break
                    
    # Print the current board
    def printBoard(self):
        for row in self.board:
            values = []
            for val in row:
                values.append(val.value)          
            print(values)

    # This function only applies after a new move is made - Forward checking
    # Function updates the domains of the corresponding row, col, and grid to the passed box
        # Also updates the degrees of the corresponding row, col, and grid
        # Degree is found based on if the value of main box is in indexed box domain
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
            # return None
            return False
        else:
            box.degree = boxDegree
        

        # Return true if updates worked and false if updates did not work
        return True

    def updateDomainAndDegreeAfterDelete(self, box: Box):
        boxRow = box.locRow
        boxCol = box.locCol

        #sets domains
        for i in range(0,9):
            # Check if box is empty and box domain contains the specified value
            if self.board[boxRow][i].value == 0:
                self.board[boxRow][i].domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                self.setDomains(boxRow, i)
                # self.setDegrees(boxRow, i)

            if self.board[i][boxCol].value == 0:
                self.board[i][boxCol].domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                self.setDomains(i, boxCol)
                # self.setDegrees(i, boxCol)

            
        gridRange = box.getGridRange()
        for i in range(gridRange[0], gridRange[1]+1):
            for j in range(gridRange[2], gridRange[3]+1):
                if self.board[i][j].value == 0:
                    self.board[i][j].domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.setDomains(i, j)
                    # self.setDegrees(i, boxCol)
        self.setDomains(boxRow, boxCol) 

        #sets degree
        for i in range(0,9):
            # Check if box is empty and box domain contains the specified value
            if self.board[boxRow][i].value == 0:
                self.setDegrees(boxRow, i)

            if self.board[i][boxCol].value == 0:
                self.setDegrees(i, boxCol)

            
        gridRange = box.getGridRange()
        for i in range(gridRange[0], gridRange[1]+1):
            for j in range(gridRange[2], gridRange[3]+1):
                if self.board[i][j].value == 0:
                    self.setDegrees(i, j)

        self.setDegrees(boxRow, boxCol) 

    # Returns an array of the boxes in the board that contain the highest degree
    # Degree Heuristic
    # Input may be altered based on if degree or mrv is found first
    def getHighestDegree(self):
        highDegreeBoxes = []
        highestDegree = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j].degree > highestDegree:
                    highDegreeBoxes.clear()
                    highestDegree = self.board[i][j].degree
                    highDegreeBoxes.append(self.board[i][j])
                elif self.board[i][j].degree == highestDegree:
                    highDegreeBoxes.append(self.board[i][j])

        return highDegreeBoxes

    # Finds the highest degree boxes based on results of MRV search
    def getHighestDegreeAfterMRV(self, mrvResults):
        highestDegreeBoxes = []
        highestDegree = 0
        for box in mrvResults:
            if box.degree > highestDegree:
                highestDegreeBoxes.clear()
                highestDegree = box.degree
                highestDegreeBoxes.append(box)
            elif box.degree == highestDegree:
                highestDegreeBoxes.append(box)

        return highestDegreeBoxes

    # Returns an array of the boxes with the lowest domain length (smallest domain)
    # MRV
    # Input may be altered based on if degree or mrv is found first
    def getLowestDomain(self):
        lowestDomainBoxes = []
        lowestDomainLength = 9
        for i in range(9):
            for j in range(9):
                if len(self.board[i][j].domain) > 0:
                    if len(self.board[i][j].domain) < lowestDomainLength:
                        lowestDomainBoxes.clear()
                        lowestDomainLength = len(self.board[i][j].domain)
                        lowestDomainBoxes.append(self.board[i][j])
                    elif len(self.board[i][j].domain) == lowestDomainLength:
                        lowestDomainBoxes.append(self.board[i][j])

        return lowestDomainBoxes
                    
    # Returns true or false whether the move was placed and forward tracking succeeded
    # Places move in baord, updates dictionaries and open spaces
    # Does forward tracking (updating degrees and domains)
        # def placeMove(self, row, col, val):
    def placeMove(self, move, val):
        row = move.locRow
        col = move.locCol
        # val = sorted(move.domain)[0]

        # Update Box
        self.board[row][col].value = val
        self.board[row][col].domain.clear()
        self.board[row][col].degree = 0

        # Update Dictionaries
        self.rowDictionary[row].append(val)
        self.colDictionary[col].append(val)
        self.gridDictionary[self.board[row][col].locGrid].append(val)

        # Decrement open spaces by 1
        self.setOpenSpaces(self.openSpaces - 1)

        # Update Domain and Degrees
        updates = self.updateDomainsAndDegrees(self.board[row][col])
        if not updates:
            return False
        
        return True

    # removes a move
    # removes a move on the baord, updates dictionaries and open spaces
        # def placeMove(self, row, col, val):
    def removeMove(self, move: Box, val):
        row = move.locRow
        col = move.locCol
        # val = sorted(move.domain)[0]

        # Update Box
        self.board[row][col].value = 0
        self.board[row][col].domain.clear()
        self.board[row][col].degree = 0

        # Update Dictionaries
        self.rowDictionary[row].remove(val)
        self.colDictionary[col].remove(val)
        self.gridDictionary[self.board[row][col].locGrid].remove(val)

        # Increment open spaces by 1
        self.setOpenSpaces(self.openSpaces + 1)

        # Update Domain and Degrees
        self.updateDomainAndDegreeAfterDelete(self.board[row][col])
        
        return True

    # Returns the next best move within the board
    # Uses mrv, degree heuristics, and tiebreaking to find move
    def findMove(self):
        move = 0
        # Find MRV (Lowest Domain)
        mrv = self.getLowestDomain()
        if len(mrv) > 1:
            # Find Degree Heuristic (Highest Degree)
            deg = self.getHighestDegreeAfterMRV(mrv)
            if len(deg) > 1:
                # Break any remaining ties
                move = tieBreak(deg)
            else:
                move = deg[0]
        else:
            move = mrv[0]

        return move


# Breaks tie within array of boxes and returns the box
def tieBreak(boxArray):
    # Find the boxes with lowest col value
    lowestCol = 8
    lowestCols = []
    for box in boxArray:
        if box.locCol < lowestCol:
            lowestCols.clear()
            lowestCol = box.locCol
            lowestCols.append(box)
        elif box.locCol == lowestCol:
            lowestCols.append(box)

    lowestRow = 8
    lowestBox = lowestCols[0]
    if len(lowestCols) > 1:
        for box in lowestCols:
            if box.locRow < lowestRow:
                lowestRow = box.locRow
                lowestBox = box
    else:
        return lowestCols[0]

    return lowestBox
    
# ------------------------------------------------------------------------------------


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