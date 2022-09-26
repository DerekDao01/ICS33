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
        pass

    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        pass

    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        pass

    def with_queens_added(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""
        #Create a new QueensState that is the same size as the original one
        newState = QueensState(self.rows, self.columns)
        newBoard = newState.board
        for position in positions:
            rowNum = position[0]
            colNum = position[1]
            if newBoard[rowNum][colNum] != "X"
                newBoard[rowNum][colNum] = "X"
            elif newBoard[rowNum][colNum] == "X":
                raise DuplicateQueenError


    def with_queens_removed(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        pass
