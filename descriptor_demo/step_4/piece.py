"""Step 4: We write a descriptor that intuitively looks like a reusable
property. It's actually not - there are caveats that we'll explore in
step 5.
"""

Black = False
White = True


class BoundedValue(object):
    """A value constrained to the 0-8 range, inclusive."""

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0 or value > 8:
            raise ValueError("value must be between 0 and 8, inclusive")
        self.value = value


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    rank = BoundedValue(0)
    file = BoundedValue(0)
    stratum = BoundedValue(0)
    era = BoundedValue(0)

    def __init__(self, color, rank=0, file=0, stratum=0, era=0):
        self.color = color
        self.rank = rank
        self.file = file
        self.stratum = stratum
        self.era = era
