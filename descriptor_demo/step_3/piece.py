"""Step 2: Using properties, we allow our chess piece to validate
its rank and file values.
"""

Black = False
White = True


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    def __init__(self, color, rank=0, file=0):
        self.color = color
        self.rank = rank
        self.file = file

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value < 0 or value > 8:
            raise ValueError("rank must be a value between 0 and 8, inclusive")
        self._rank = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        if value < 0 or value > 8:
            raise ValueError("file must be a value between 0 and 8, inclusive")
        self._file = value
