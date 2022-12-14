# queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# A module containing tools that could assist in solving variants of the
# well-known "n-queens" problem.  Note that we're only implementing one part
# of the problem: immutably managing the "state" of the board (i.e., which
# queens are arranged in which cells).
#
# Your goal is to complete the QueensState class described below, though
# you'll need to build it incrementally, as well as test it incrementally by
# writing unit tests in test_queens.py.  Make sure you've read the project
# write-up before you proceed, as it will explain the requirements around
# following (and documenting) an incremental process of solving this problem.
#
# DO NOT MODIFY THE Position NAMEDTUPLE OR THE PROVIDED EXCEPTION CLASSES.

from collections import namedtuple
import copy

Position = namedtuple('Position', ['row', 'column'])

# Ordinarily, we would write docstrings within classes or their methods.
# Since a namedtuple builds those classes and methods for us, we instead
# add the documentation by hand afterward.
Position.__doc__ = 'A position on a chessboard, specified by zero-based row and column numbers.'
Position.row.__doc__ = 'A zero-based row number'
Position.column.__doc__ = 'A zero-based column number'



class DuplicateQueenError(Exception):
    """An exception indicating an attempt to add a queen where one is already present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where the duplicate queen exists."""
        self._position = position

    def __str__(self) -> str:
        return f'duplicate queen in row {self._position.row} column {self._position.column}'


class MissingQueenError(Exception):
    """An exception indicating an attempt to remove a queen where one is not present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where a queen is missing."""
        self._position = position


    def __str__(self) -> str:
        return f'missing queen in row {self._position.row} column {self._position.column}'



class QueensState:
    """Immutably represents the state of a chessboard being used to assist in
    solving the n-queens problem."""

    def __init__(self, rows: int, columns: int):
        """Initializes the chessboard to have the given numbers of rows and columns,
        with no queens occupying any of its cells."""
        #assuming an n x m board, the board will be a list with n lists (n rows), each of m size (m columns).
        self.rows = rows
        self.columns = columns
        self.board = []
        #Append the "rows" to the board variable
        for i in range(self.rows):
            rowLst = []
            for j in range(self.columns):
                rowLst.append("O")  #Append an "O" string to each row. This means there is no queen yet
                #If there is a queen, it will be "X"
            self.board.append(rowLst)

    def queen_count(self) -> int:
        """Returns the number of queens on the chessboard."""
        self.queenCounter = 0
        for row in self.board:
            for space in row:
                if space == "X":
                    self.queenCounter += 1
        return self.queenCounter

    def queens(self) -> list[Position]:
        """Returns a list of the positions in which queens appear on the chessboard,
        arranged in no particular order."""
        #Initialize the list that will be returned
        queenLst = []
        board = self.board
        #Check every space on the board to see if it's a queen
        for i, row in enumerate(board):   #i will refer to the row number
            for j, space in enumerate(row):    #j will refer to the column number
                if space == "X": #"X" is queen
                    pos = Position(i,j)
                    queenLst.append(pos)
        return queenLst

    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        #Make a note of the row and column position
        rowNum = position[0]
        colNum = position[1]
        if self.board[rowNum][colNum] == "X":
            return True
        else:
            return False

    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        board = self.board
        for i, row in enumerate(board):
            for j, space in enumerate(row):
                if space == "X": #If the space is a queen, check to see if it's unsafe
                    #check the same row and column by looking for equal i & j values
                    for k, row in enumerate(board):
                        for l, space in enumerate(row):
                            #If theres another queen, check if it has the same
                            #row or column as the original, but not the same exact coordinate
                            if (space == "X" and k == i) and (l != j):
                                return True
                            elif (space == "X" and l == j) and (k != i):
                                return True
                            #Check diagonals
                            #If theres another queen and the difference between
                            #their horizontal and vertical spaces are the same, it can be captured
                            elif (space == "X") and (i != k and l != j):
                                rowDif = abs(k-i)
                                colDif = abs(l-j)
                                if rowDif == colDif:
                                    return True
        return False

    def with_queens_added(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""
        #Create a new QueensState that is the same size as the original one
        newState = QueensState(self.rows, self.columns)
        #Copy the board of the original QueensState
        newState.board = copy.deepcopy(self.board)
        newBoard = newState.board
        for position in positions:
            rowNum = position[0]
            colNum = position[1]
            #If the space doesn't already have a queen, put one
            if newBoard[rowNum][colNum] != "X":
                newBoard[rowNum][colNum] = "X"
            #If it does have a queen, raise the error
            elif newBoard[rowNum][colNum] == "X":
                raise DuplicateQueenError(position)
        return newState

    def with_queens_removed(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        #Create a new QueensState that is the same size as the original one
        newState = QueensState(self.rows, self.columns)
        #Copy the board of the original QueensState
        newState.board = copy.deepcopy(self.board)
        newBoard = newState.board
        #Create a variable to track how many queens are on the board before removing them
        queenCounter = 0
        for position in positions:
            rowNum = position[0]
            colNum = position[1]
            #If the space has a queen, remove it
            if newBoard[rowNum][colNum] == "X":
                queenCounter += 1
                newBoard[rowNum][colNum] = "O"
            #If the method did not detect a queen in a given position, raise the error
            elif newBoard[rowNum][colNum] == "O":
                raise MissingQueenError(position)
        return newState