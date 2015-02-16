"""Step 1: We create a chess piece base class that can store a few
useful pieces of information universal to all chess pieces.
"""

Black = False
White = True


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    def __init__(self, color, rank=0, file=0):
        self.color = color
        self.rank = rank
        self.file = file
