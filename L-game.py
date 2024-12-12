import json

class AllPossibleMoves:
    listDir = {'N', 'E', 'S', 'W'}
    listMoves = {
                (1, 1, 'S'), (1, 1, 'E'),
                (2, 1, 'S'), (2, 1, 'E'), (2, 1, 'W'),
                (3, 1, 'S'), (3, 1, 'E'), (3, 1, 'W'),
                (4, 1, 'S'), (4, 1, 'W'),
                (1, 2, 'N'), (1, 2, 'S'), (1, 2, 'E'),
                (2, 2, 'N'), (2, 2, 'S'), (2, 2, 'E'), (2, 2, 'W'),
                (3, 2, 'N'), (3, 2, 'S'), (3, 2, 'E'), (3, 2, 'W'),
                (4, 2, 'N'), (4, 2, 'S'), (4, 2, 'W'),
                (1, 3, 'N'), (1, 3, 'S'), (1, 3, 'E'),
                (2, 3, 'N'), (2, 3, 'S'), (2, 3, 'E'), (2, 3, 'W'),
                (3, 3, 'N'), (3, 3, 'S'), (3, 3, 'E'), (3, 3, 'W'),
                (4, 3, 'N'), (4, 3, 'S'), (4, 3, 'W'),
                (1, 4, 'N'), (1, 4, 'E'),
                (2, 4, 'N'), (2, 4, 'E'), (2, 4, 'W'),
                (3, 4, 'N'), (3, 4, 'E'), (3, 4, 'W'),
                (4, 4, 'N'), (4, 4, 'W'),
    }
    listMove = [
                (1, 1, 'S'), (1, 1, 'E'),
                (2, 1, 'S'), (2, 1, 'E'), (2, 1, 'W'),
                (3, 1, 'S'), (3, 1, 'E'), (3, 1, 'W'),
                (4, 1, 'S'), (4, 1, 'W'),
                (1, 2, 'N'), (1, 2, 'S'), (1, 2, 'E'),
                (2, 2, 'N'), (2, 2, 'S'), (2, 2, 'E'), (2, 2, 'W'),
                (3, 2, 'N'), (3, 2, 'S'), (3, 2, 'E'), (3, 2, 'W'),
                (4, 2, 'N'), (4, 2, 'S'), (4, 2, 'W'),
                (1, 3, 'N'), (1, 3, 'S'), (1, 3, 'E'),
                (2, 3, 'N'), (2, 3, 'S'), (2, 3, 'E'), (2, 3, 'W'),
                (3, 3, 'N'), (3, 3, 'S'), (3, 3, 'E'), (3, 3, 'W'),
                (4, 3, 'N'), (4, 3, 'S'), (4, 3, 'W'),
                (1, 4, 'N'), (1, 4, 'E'),
                (2, 4, 'N'), (2, 4, 'E'), (2, 4, 'W'),
                (3, 4, 'N'), (3, 4, 'E'), (3, 4, 'W'),
                (4, 4, 'N'), (4, 4, 'W'),
    ]

def testAllPossibleMove():
    testGame = LGame()
    testGame.neutrals = []
    testGame.player1 = ()
    testGame.gridArray = [
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'], ]
    with open("output.txt", "w") as text_file:
        for i in range(len(AllPossibleMoves.listMove)):
            move = AllPossibleMoves.listMove[i]
            text_file.write('========\n')
            text_file.write(str(move[0]) + ' ' + str(move[1]) + ' '  + str(move[2]) + '\n')
            testGame.commitLPieceMove(move[0], move[1], move[2])
            text_file.write(testGame.textPrintGameGrid())
            testGame.whoseTurn = 1
            testGame.deleteCurrPlayerFromGrid()

def gamestateToBoard(gamestate):
    listState = list(gamestate)
    newGame = LGame(listState[0], listState[1], listState[2], listState[3], listState[4])
    return newGame

class LGame:
    """
    The overall game. Holds data for the playing grid as well as where each element is placed.
    Will primarily hold 4 variables:
        Position of player 1's L-piece
        Position of player 2's L-piece
        Position of neutral piece #1
        Position of neutral piece #2
    """
    # def __init__(self):
    #     """
    #     Initialize the starting locations for the L-pieces and neutral pieces.
    #     """
    #     self.player1 = (1, 2, 'S') # The red player
    #     self.player2 = (4, 3, 'N') # The blue player
    #     self.neutrals = [(1, 1), (4, 4)]
    #     self.whoseTurn = 1
    #     self.gridArray = [
    #         ['X', '-', '-', '-'],
    #         ['R', 'R', 'R', 'B'],
    #         ['R', 'B', 'B', 'B'],
    #         ['-', '-', '-', 'X'], ]

    def __init__(self, turn=1, player1=(1,2,'S'), player2=(4, 3, 'N'), neutral1=(1,1), neutral2=(4,4)):
        self.player1 = player1 # The red player (1, 2, 'S')
        self.player2 = player2 # The blue player (4, 3, 'N')
        self.neutrals = [(1,1), (4,4)]
        self.whoseTurn = 1
        self.gridArray = [
            ['X', '-', '-', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', 'X'], ]
        
        player1, player2 = list(player1), list(player2)
        neutral1, neutral2 = list(neutral1), list(neutral2)
        self.commitLPieceMove(player1[0], player1[1], player1[2])
        self.commitLPieceMove(player2[0], player2[1], player2[2])
        self.whoseTurn = turn
        self.commitNeutralMove(1, 1, neutral1[0], neutral1[1])
        self.commitNeutralMove(4, 4, neutral2[0], neutral2[1])
    
    def getLegalActions(self):
        possibleMoves = []
        for move in AllPossibleMoves.listMoves:
            if self.checkIsLegalMove(move[0], move[1], move[2]):
                possibleMoves.append(move)
                firstNPiece = list(self.neutrals[0])
                secondNPiece = list(self.neutrals[1])
                player = self.whoseTurn
                if player == 1:
                    prevMove = self.player1
                elif player == 2:
                    prevMove = self.player2
                self.deleteCurrPlayerFromGrid()

                self.commitLPieceMove(move[0], move[1], move[2])
                for row in range(4):
                    for col in range(4):
                        if self.gridArray[row][col] == '-':
                            possibleMoves.append((move[0], move[1], move[2], firstNPiece[0], firstNPiece[1], col + 1, row + 1))
                            possibleMoves.append((move[0], move[1], move[2], secondNPiece[0], secondNPiece[1], col + 1, row + 1))
                self.whoseTurn = player
                if player == 1:
                    self.player1 = prevMove
                elif player == 2:
                    self.player2 = prevMove
        return possibleMoves
            
    def isGameOver(self):
        if self.numPossibleMoves() == 0:
            return True
        else:
            return False
    
    def evalFunction(self):
        player = self.whoseTurn
        self.whoseTurn = 1
        i1 = self.numPossibleMoves()
        self.whoseTurn = 2
        i2 = self.numPossibleMoves()
        self.whoseTurn = player
        return (i1, i2)

    def numPossibleMoves(self):
        for move in AllPossibleMoves.listMoves:
            if self.checkIsLegalMove(move[0], move[1], move[2]):
                i += 1
        return i

    def checkIsLegalMove(self, x, y, dir, nPreX = None, nPreY = None, nPostX = None, nPostY = None):
        # Delete the player we are checking for from the grid so we can accurately check if the move is legal
        self.deleteCurrPlayerFromGrid()

        # Store the move we are checking in a tuple
        move = (x, y, dir)
        # Store the row and column in a zero-based value to use when accessing the array.
        arrRow, arrCol = y - 1, x - 1

        # Check if the move is a possible move from list of all possible moves
        if move not in AllPossibleMoves.listMoves:
            return False
        
        # If the move is the same as the move they already did, then return false
        if (self.whoseTurn == 1 and move == self.player1) or (self.whoseTurn == 2 and move == self.player2):
            return False
        
        # Check if the neutral piece move is legal
        if nPreX == None or nPreY != None or nPostX == None or nPostY == None:
            hasNeutralMove = False
        else:
            hasNeutralMove = True
        if hasNeutralMove:
            nPrevCoord = (nPreX, nPreY)
            if nPrevCoord not in self.neutrals:
                print("Neutral piece did not start there")
                return False
            if nPrevCoord == (x, y):
                print("Neutral piece overlap with L move")
                return False

        if self.gridArray[arrRow][arrCol] != '-':
            return False

        nPostCoord = (nPostX, nPostY)
        # Check if the L-piece move conflicts with neutral or enemy L-piece
        match dir:
            case 'N':
                # Check top
                if nPostCoord == (x, y - 1):
                    print("Neutral piece overlap with L move")
                    return False
                if self.gridArray[arrRow - 1][arrCol] != '-':
                    return False
                if x <= 2:
                    # Check right-long
                    if nPostCoord == (x + 1, y) or nPostCoord == (x + 2, y):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow][arrCol + 1] != '-' or self.gridArray[arrRow][arrCol + 2] != '-':
                        return False
                else:
                    # Check left-long
                    if nPostCoord == (x - 1, y) or nPostCoord == (x - 2, y):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow][arrCol - 1] != '-' or self.gridArray[arrRow][arrCol - 2] != '-':
                        return False
            case 'S':
                # Check bottom
                if nPostCoord == (x, y + 1):
                    print("Neutral piece overlap with L move")
                    return False
                if self.gridArray[arrRow + 1][arrCol] != '-':
                    return False
                if x <= 2:
                    # Check right-long
                    if nPostCoord == (x + 1, y) or nPostCoord == (x + 2, y):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow][arrCol + 1] != '-' or self.gridArray[arrRow][arrCol + 2] != '-':
                        return False
                else:
                    # Check left-long
                    if nPostCoord == (x - 1, y) or nPostCoord == (x - 2, y):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow][arrCol - 1] != '-' or self.gridArray[arrRow][arrCol - 2] != '-':
                        return False
            case 'E':
                # Check right
                if nPostCoord == (x + 1, y):
                    print("Neutral piece overlap with L move")
                    return False
                if self.gridArray[arrRow][arrCol + 1] != '-':
                    return False
                if y <= 2:
                    # Check down-long
                    if nPostCoord == (x, y + 1) or nPostCoord == (x, y + 2):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow + 1][arrCol] != '-' or self.gridArray[arrRow + 2][arrCol] != '-':
                        return False
                else:
                    # Check up-long
                    if nPostCoord == (x, y - 1) or nPostCoord == (x, y - 2):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow - 1][arrCol] != '-' or self.gridArray[arrRow - 2][arrCol] != '-':
                        return False
            case 'W':
                # Check left
                if self.gridArray[arrRow][arrCol - 1] != '-':
                    return False
                if y <= 2:
                    # Check down-long
                    if nPostCoord == (x, y + 1) or nPostCoord == (x, y + 2):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow + 1][arrCol] != '-' or self.gridArray[arrRow + 2][arrCol] != '-':
                        return False
                else:
                    # Check up-long
                    if nPostCoord == (x, y - 1) or nPostCoord == (x, y - 2):
                        print("Neutral piece overlap with L move")
                        return False
                    if self.gridArray[arrRow - 1][arrCol] != '-' or self.gridArray[arrRow - 2][arrCol] != '-':
                        return False
        
        # If it passed all the previous tests, then it is a legal move
        return True
        
    def printGameGrid(self):
        # Prints the grid across 4 lines. Also prints a divider
        print("=======")
        for i in range(4):
            printString = ""
            for j in range(4):
                printString += str(self.gridArray[i][j])
                printString += ' '
            print(printString)

    def textPrintGameGrid(self):
        # Prints the grid across 4 lines. Also prints a divider
        printString = ""
        for i in range(4):
            for j in range(4):
                printString += str(self.gridArray[i][j])
                printString += ' '
            printString += '\n'
        return printString

    def deleteCurrPlayerFromGrid(self):
        # Deletes the current player's letter from the grid
        # There move is still saved in memory in self.player1 or self.player2
        if self.whoseTurn == 1:
            deleteChar = 'R'
        elif self.whoseTurn == 2:
            deleteChar = 'B'
        for i in range(4):
            for j in range(4):
                if self.gridArray[i][j] == deleteChar:
                    self.gridArray[i][j] = '-'

    def getInputMove(self):
        # Keep on trying for input until we get a valid input
        while True:
            move = input("Where would you like to move?\n")
            if move.upper() == 'Q':
                return 'Q'
            move = move.split()
            # If they input wrong number of elements
            if len(move) != 3:
                if len(move) != 7:
                    print("Invalid input form. Incorrect number of arguments.")
                    continue

            # If first two (x,y) are not numbers, try again
            if not move[0].isnumeric() or not move[1].isnumeric():
                print("Invalid input form. Example Input: '2 1 E 1 1 2 4' OR '2 1 E'")
                continue
            row, col, direc = int(move[0]), int(move[1]), move[2].upper()

            # If 3rd element is not a direction, try again
            if direc not in AllPossibleMoves.listDir:
                print("Impossilbe move.")
                continue
            legalXY = range(1,5)

            # Check if first two numbers are in the grid
            if row not in legalXY or col not in legalXY:
                print("Outside of grid. Must be between (1,1) and (4,4).")
                continue

            # Check if all cases for last 4 optional numbers
            if len(move) == 7:
                # Check they are all numbers
                if not move[3].isnumeric() or not move[4].isnumeric() or not move[5].isnumeric() or not move[6].isnumeric():
                    print("Invalid input form. Example Input: '2 1 E 1 1 2 4' OR '2 1 E'")
                    continue
                neutPreX, neutPreY, neutPostX, neutPostY = int(move[3]), int(move[4]), int(move[5]), int(move[6])

                # Check that all the numbers are between [1,4]
                if neutPreX not in legalXY or neutPreY not in legalXY or neutPostX not in legalXY or neutPostY not in legalXY:
                    print("Outside of grid. Must be between (1,1) and (4,4).")
                    continue
                else:
                    # Return the full 7 arguments (yes neutral piece move)
                    return (row, col, direc, int(move[3]), int(move[4]), int(move[5]), int(move[6]))
            # Return only 3 arguments (no neutral piece move)
            return (row, col, direc)

    def commitLPieceMove(self, x, y, dir):
        arrRow = y - 1
        arrCol = x - 1
        if self.whoseTurn == 1:
            writeChar = 'R'
            self.player1 = (x, y, dir)
        elif self.whoseTurn == 2:
            writeChar = 'B'
            self.player2 = (x, y, dir)
        
        self.gridArray[arrRow][arrCol] = writeChar
        match dir:
            case 'N':
                self.gridArray[arrRow - 1][arrCol] = writeChar
                if x <= 2:
                    self.gridArray[arrRow][arrCol + 1] = writeChar
                    self.gridArray[arrRow][arrCol + 2] = writeChar
                else:
                    self.gridArray[arrRow][arrCol - 1] = writeChar
                    self.gridArray[arrRow][arrCol - 2] = writeChar
            case 'S':
                self.gridArray[arrRow + 1][arrCol] = writeChar
                if x <= 2:
                    self.gridArray[arrRow][arrCol + 1] = writeChar
                    self.gridArray[arrRow][arrCol + 2] = writeChar
                else:
                    self.gridArray[arrRow][arrCol - 1] = writeChar
                    self.gridArray[arrRow][arrCol - 2] = writeChar
            case 'E':
                self.gridArray[arrRow][arrCol + 1] = writeChar
                if y <= 2:
                    # down long
                    self.gridArray[arrRow + 1][arrCol] = writeChar
                    self.gridArray[arrRow + 2][arrCol] = writeChar
                else:
                    # up long
                    self.gridArray[arrRow - 1][arrCol] = writeChar
                    self.gridArray[arrRow - 2][arrCol] = writeChar
            case 'W':
                self.gridArray[arrRow][arrCol - 1] = writeChar
                if y <= 2:
                    # down long
                    self.gridArray[arrRow + 1][arrCol] = writeChar
                    self.gridArray[arrRow + 2][arrCol] = writeChar
                else:
                    # up long
                    self.gridArray[arrRow - 1][arrCol] = writeChar
                    self.gridArray[arrRow - 2][arrCol] = writeChar
        if self.whoseTurn == 1:
            self.whoseTurn = 2
        else:
            self.whoseTurn = 1
              
    def checkIsNeutralLegalMove(self, prevX, prevY, newX, newY):
        newArrRow, newArrCol = newY - 1, newX - 1
        if (prevX, prevY) in self.neutrals:
            if self.gridArray[newArrRow][newArrCol] == '-':
                return True
        else:
            return False

    def commitNeutralMove(self, prevX, prevY, newX, newY):
        oldArrRow, oldArrCol = prevY - 1, prevX - 1
        newArrRow, newArrCol = newY - 1, newX - 1
        self.neutrals.remove((prevX, prevY))
        self.neutrals.append((newX, newY))
        self.gridArray[oldArrRow][oldArrCol] = '-'
        self.gridArray[newArrRow][newArrCol] = 'X'

    def undoDeleteMove(self):
        if self.whoseTurn == 1:
            self.commitLPieceMove(self.player1[0], self.player1[1], self.player1[2])
            self.whoseTurn = 1
        else:
            self.commitLPieceMove(self.player2[0], self.player2[1], self.player2[2])
            self.whoseTurn = 2

    def gamestate(self):
        state = []
        state.append(self.whoseTurn)
        state.append(self.player1)
        state.append(self.player2)
        state.append(self.neutrals[0])
        state.append(self.neutrals[1])
        return tuple(state)

    def aiGameLoop(self):
        while True:
            if self.isGameOver():
                print("Player " + str(self.whoseTurn) + " has no more possible moves.")
                if self.whoseTurn == 1:
                    opp = '2'
                else:
                    opp = '1'
                print("Player " + opp + " is the winner!")
                break
            if self.whoseTurn == 1:
                self.printGameGrid()
                move = self.getInputMove()
                if move == 'Q' or move == 'q':
                    print("Quitting out of the game")
                    break
                listMove = [None, None, None, None, None, None, None]
                for i in range(len(move)):
                    listMove[i] = move[i]
                if self.checkIsLegalMove(listMove[0], listMove[1], listMove[2]):
                    self.commitLPieceMove(listMove[0], listMove[1], listMove[2])
                else:
                    print("Not a legal move")
                    self.undoDeleteMove()
                    continue
                # if the user inputted enough arguments for a neutral piece move, test if legal neutral piece move
                if len(move) == 7:
                    if self.checkIsNeutralLegalMove(listMove[3], listMove[4], listMove[5], listMove[6]):
                        self.commitNeutralMove(listMove[3], listMove[4], listMove[5], listMove[6])
                
                else:
                    self.undoDeleteMove()
            elif self.whoseTurn == 2:
                score = -999999
                for move in self.getLegalActions():
                    tempScore = self.greedySearchScore(move, self.gamestate())
                    if tempScore > score:
                        bestMove = move
                        score = tempScore
                bestMove = list(bestMove)
                self.commitLPieceMove(bestMove[0], bestMove[1], bestMove[2])
                if len(bestMove) == 7:
                    self.commitNeutralMove(bestMove[3], bestMove[4], bestMove[5], bestMove[6])

                
        # self.dictTerminalStates = {}
        # while True:
        #     for move in AllPossibleMoves.listMove:

        #         if self.gamestate not in self.dictTerminalStates:
        #             if self.isGameOver() and self.whoseTurn == 1:
        #                 self.dictTerminalStates[self.gamestate] = 1
        #             elif self.isGameOver() and self.whoseTurn == 2:
        #                 self.dictTerminalStates[self.gamestate] = -1

    def greedySearchScore(self, move, gamestate):
        move = list(move)
        listMove = [None, None, None, None, None, None, None]
        for i in range(len(move)):
            listMove[i] = move[i]
        tempGame = gamestateToBoard(gamestate)
        tempGame.commitLPieceMove(move[0], move[1], move[2])
        return tempGame.numPossibleMoves()
        

    def recurAIPlay(self, gamestate, m, depth):
        if gamestate in dictTerminalStates:
            return (m, dictTerminalStates[gamestate] * 1000000)
        if gamestate in dictNumMoves:
            return (m, dictTerminalStates[gamestate])
        newGame = gamestateToBoard(gamestate)
        if newGame.isGameOver():
            if newGame.whoseTurn == 1:
                dictTerminalStates[newGame.gamestate()] = -1
            elif newGame.whoseTurn == 2:
                dictTerminalStates[newGame.gamestate()] = 1
        elif depth >= maxDepth:
            return 0
        else:
            m = list(m)
            # print(m)
            newGame.commitLPieceMove(m[0], m[1], m[2])
            if len(m) > 3:
                newGame.commitNeutralMove(m[3], m[4], m[5], m[6])
            # newGame.printGameGrid()
            for move in newGame.getLegalActions():
                newGame.recurAIPlay(newGame.gamestate(), move, depth + 1)

    def aivsai(self):
        for move in self.getLegalActions():
            self.recurAIPlay(self.gamestate(), move, 0)
        print(dictTerminalStates)


    def mainGameLoop(self):
        while True:
            self.printGameGrid()
            move = self.getInputMove()
            if move == 'Q' or move == 'q':
                print("Quitting out of the game")
                break
            listMove = [None, None, None, None, None, None, None]
            for i in range(len(move)):
                listMove[i] = move[i]
            if self.checkIsLegalMove(listMove[0], listMove[1], listMove[2]):
                self.commitLPieceMove(listMove[0], listMove[1], listMove[2])
            else:
                print("Not a legal move")
                self.undoDeleteMove()
                continue
            # if the user inputted enough arguments for a neutral piece move, test if legal neutral piece move
            if len(move) == 7:
                if self.checkIsNeutralLegalMove(listMove[3], listMove[4], listMove[5], listMove[6]):
                    self.commitNeutralMove(listMove[3], listMove[4], listMove[5], listMove[6])
            if self.isGameOver():
                print("Player " + str(self.whoseTurn) + " has no more possible moves.")
                if self.whoseTurn == 1:
                    opp = '2'
                else:
                    opp = '1'
                print("Player " + opp + " is the winner!")
                break
            else:
                self.undoDeleteMove()

myGame = LGame()
# myGame.printGameGrid()
# print(myGame.getLegalActions())

# gamestateToBoard(myGame.gamestate())
keepLoop = True
with open('terminal.json') as f:
    dictTerminalStates = json.load(f)
with open('numMoves.json') as g:
    dictNumMoves = json.load(g)
maxDepth = 2
while keepLoop:
    answer = input("Would you like to play against a person (1) or an AI (2) or AI vs AI (3)? ")
    if answer == '1' or answer == '2' or answer == '3':
        keepLoop = False
    else:
        print("Please input either '1' or '2' or '3'")
if answer == '1':
    myGame.mainGameLoop()
elif answer == '2':
    myGame.aiGameLoop()
elif answer == '3':
    myGame.aivsai()

# myGame = gamestateToBoard((2, (2, 2, 'S'), (3, 4, 'N'), (1,3), (4, 3)))
# myGame.printGameGrid()