"""Step 5: We modify our descriptor to use a WeakKeyDictionary, so that
it can hold a different value for every Piece instance.

Credit for the WeakKeyDictionary method goes to Chris Beaumont in his
article "Python Descriptors Demystified."
http://nbviewer.ipython.org/gist/ChrisBeaumont/5758381/descriptor_writeup.ipynb
"""

from weakref import WeakKeyDictionary

Black = False
White = True


class BoundedValue(object):
    """A value constrained to the 0-8 range, inclusive."""

    def __init__(self):
        self.values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.values[instance]

    def __set__(self, instance, value):
        if value < 0 or value > 8:
            raise ValueError("value must be between 0 and 8, inclusive")
        self.values[instance] = value


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    rank = BoundedValue()
    file = BoundedValue()
    stratum = BoundedValue()
    era = BoundedValue()

    def __init__(self, color, rank=0, file=0, stratum=0, era=0):
        self.color = color
        self.rank = rank
        self.file = file
        self.stratum = stratum
        self.era = era
