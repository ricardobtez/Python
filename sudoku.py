# Author: Ricardo Benitez
# Sudoku solved as constrain satisfaction problem

from queue import LifoQueue

MAX_ITER = 1000

class Sudoku:
    def __init__(self,problem):
        self.n = 9
        self.board = problem

    def getBoard(self):
        return self.board
    def setBoard(self, board):
        self.board = board[:]
    def display(self):
        print('-'*12)
        for y in range(self.n):
            line = ''
            for x in range(self.n):
                line += str(self.board[y][x])  if (0 != self.board[y][x]) else ' '
                if(((x+1)%3) == 0 and
                    x is not 0):
                    line += '|'
            if((y%3) == 0 and
                y is not 0):
                print('-'*12)
            print(line)
        print('-'*12)

class CSPSudoku:
    def __init__(self, initialState):
        self.stack = LifoQueue()
        self.initial = initialState
    def solve(self):
        retValue = self.initial[:]
        solved = False
        while(not solved):
            # self.__isValidInBlock(9,1,self.initial)
            # self.__isValidInRow(9,0,self.initial)
            # self.__isValidInColumn(9,0,self.initial)
            print(self.getPossibleValues(2,3,self.initial))
            break
        return retValue
    def constrainCheck(self, board):
        pass

    def __isValidInBlock(self, number, block, board):
        boReturn = False
        if(block < 9):
            boReturn = True
            hor = block%3
            ver = (block//3)*3 # I know, looks stupid, trust me on this
            for i in range(3):
                localBoard = board[ver+i][hor*3:hor*3+3]
                if(number in localBoard):
                    boReturn = False
                    break
        return boReturn
    def __isValidInRow(self, number, row, board):
        boReturn = False
        if(row < 9):
            boReturn = False if(number in board[row]) else True
        return boReturn
    def __isValidInColumn(self, number, column, board):
        boReturn = False
        if(column < 9):
            boReturn = True
            for i in range(9):
                if(board[i][column] == number):
                    boReturn = False
                    break
        return boReturn
    # Auxiliary function not used by CSP
    def getPossibleValues(self, x, y, board):
        returnList = []
        if(0 == board[y][x]):
            for number in range(1,10,1):
                block = ((y//3)*3) + ((x//3))
                print("number:{} and block:{}".format(number, block))
                if(self.__isValidInBlock(number,block, board) and
                   self.__isValidInRow(number, y, board) and
                   self.__isValidInColumn(number, x, board)):
                    returnList.append(number)
        return returnList

def init():
    inFileHdlr = open('sudokuProblem.txt', 'r')
    prob = []
    for line in inFileHdlr:
        prob.append([int(x) for x in line.strip()])
    return prob
 
if __name__ == '__main__':
    print('Sudoku')
    prob = init()
    sud = Sudoku(prob)
    sud.display()
    csp = CSPSudoku(prob)
    solutions = csp.solve()
