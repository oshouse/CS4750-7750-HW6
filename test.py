from board import GameBoard
# from box import Box

# Main Test
def mainTest():
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
    


# Run Tests
mainTest()