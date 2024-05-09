"""
R1: Our board will be in the shape of a rectangle.
R2: All pieces will have four sides that can either have an indentation, an extrusion, or a flat edge.
R3: There are four corner pieces, some edge pieces, and the remaining ones are the middle pieces. A corner piece has two flat sides, an edge piece only has one flat side, and a middle piece doesn’t have any flat edge.
R4: All pieces will be unique, so only one piece will fit with one other piece.
R5: Two pieces fit together by the curvature of the indentation on one piece matching up to the curvature of the extrusion on another.
"""

from enum import Enum

class Unit(Enum):
    EDGE = 1
    MIDDLE = 2
    CORNER = 3
    
        
class Piece:
    def __init__(self):
        self.sides = 4 * [None]
        
    def check_corner(self):
        pass
        
    def check_middle(self):
        pass
        
    def check_edge(self):
        pass
    
class PuzzleSolver:
  # board here refers to the instance of the Puzzle board
  def match_pieces(self, board):
    # Returns the Puzzle board
    pass


class __Singleton(type):
    __instances = None

    # Puzzle is a singleton class that ensures it will have only one active instance at a time
    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super().__call__(*args, **kwargs)
        return cls.__instances


class Puzzle(metaclass=__Singleton):
    def __init__(self):
        self.__board = [[]] # List of List of Piece (2D array)
        self.__free = [] # List of Piece for currently free pieces (yet to be inserted in board)

    def insert_piece(self, piece, row, column):
        pass
    
if __name__ == "__main__":
    s = __Singleton()
    print(s)