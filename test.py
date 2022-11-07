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
    # degrees = board1.getHighestDegree()
    # domains = board1.getLowestDomain()

    # for box in degrees:
    #     box.printBox()

    # for box in domains:
    #     box.printBox()

    move = board1.findMove()
    move.printBox()

    # worked = board1.placeMove(move.locRow, move.locCol, sorted(move.domain)[0])
    worked = board1.placeMove(move)
    if worked:
        board1.printBoard()

    move2 = board1.findMove()
    move2.printBox()
    # worked2 = board1.placeMove(move2.locRow, move2.locCol, sorted(move2.domain)[0])
    worked2 = board1.placeMove(move2)
    if worked2:
        board1.printBoard()


# Run Tests
mainTest()