"""Step 3: Add strata and era properties. Things are getting crowded."""

Black = False
White = True


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    def __init__(self, color, rank=0, file=0, stratum=0, era=0):
        self.color = color
        self.rank = rank
        self.file = file
        self.stratum = stratum
        self.era = era

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

    @property
    def stratum(self):
        return self._stratum

    @stratum.setter
    def stratum(self, value):
        if value < 0 or value > 8:
            raise ValueError("stratum must be a value between 0 and 8, inclusive")
        self._stratum = value

    @property
    def era(self):
        return self._era

    @era.setter
    def era(self, value):
        if value < 0 or value > 8:
            raise ValueError("era must be a value between 0 and 8, inclusive")
        self._era = value
