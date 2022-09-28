# test_queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import *
import unittest

class TestQueensState(unittest.TestCase):
    def test_zero_queen_count_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_queen_count_not_zero(self):
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,2)
        positions = [pos1, pos2]
        newState = state.with_queens_added(positions)
        self.assertEqual(newState.queen_count(), 2)

    def test_with_queens_added(self):
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,2)
        pos3 = Position(2,2)
        positions = [pos1, pos2, pos3]
        try:
            newState = state.with_queens_added(positions)
        except DuplicateQueenError as DupQueen:
            self.assertEqual(str(DupQueen), 'duplicate queen in row 2 column 2')

    def test_with_queens_removed(self):
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,2)
        pos3 = Position(3,3)
        positions1 = [pos1, pos2] #Use this to create the second board.
        positions2 = [pos1, pos2, pos3]   #Use this to remove queens. Expecting an error
        try:
            newState1 = state.with_queens_added(positions1)
            newState2 = newState1.with_queens_removed(positions2)
        except MissingQueenError as MisQueen:
            self.assertEqual(str(MisQueen), 'missing queen in row 3 column 3')

    def test_has_queen_true(self):
        #Test if there is a queen at a certain position: expecting value to be true
        state = QueensState(8, 8)
        pos1 = Position(1, 1)
        positions = [pos1]
        newState = state.with_queens_added(positions)
        self.assertEqual(newState.has_queen(pos1), True)

    def test_has_queen_false(self):
        #Test if there is a queen at a certain position: expecting value to be false
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,2)
        positions = [pos1]
        newState = state.with_queens_added(positions)
        self.assertEqual(newState.has_queen(pos2), False)

    def test_queens(self):
        #Test to see if the function Queens can detect which spaces have queens
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,2)
        positions1 = [pos1, pos2] #positions1 is just the list of positions when we make our object
        newState = state.with_queens_added(positions1)
        positions2 = newState.queens() #positions2 returns the positions of the queens on the board
        self.assertEqual(positions1, positions2)

    def test_queens_unsafe_horizontal(self):
        #Tests to see if any queens on the board can be captured horizontally
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(2,1) #Tests horizontals
        positions = [pos1, pos2]
        newState = state.with_queens_added(positions)
        capturable = newState.any_queens_unsafe()
        self.assertEqual(capturable, True)

    def test_queens_unsafe_vertical(self):
        state = QueensState(8,8)
        pos1 = Position(1,1)
        pos2 = Position(1,2) #Tests verticals
        positions = [pos1, pos2]
        newState = state.with_queens_added(positions)
        capturable = newState.any_queens_unsafe()
        self.assertEqual(capturable, True)



if __name__ == '__main__':
    unittest.main()
