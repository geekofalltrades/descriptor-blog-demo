"""Step 6: I experiment with a different way of tying descriptors to
specific instances. Here, I've created a factory function that creates
descriptors which store their value in a certain attribute on their
class instance.
"""

Black = False
White = True


def bounded_value_factory(name):
    """Factory function for BoundedValues. Creates BoundedValues which
    store their data in the named attribute on the instance in which
    they're accessed.
    """

    class BoundedValue(object):
        """A value constrained to the 0-8 range, inclusive."""

        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            if value < 0 or value > 8:
                raise ValueError("value must be between 0 and 8, inclusive")
            setattr(instance, self.name, value)

    return BoundedValue(name)


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    rank = bounded_value_factory('_rank')
    file = bounded_value_factory('_file')
    stratum = bounded_value_factory('_stratum')
    era = bounded_value_factory('_era')

    def __init__(self, color, rank=0, file=0, stratum=0, era=0):
        self.color = color
        self.rank = rank
        self.file = file
        self.stratum = stratum
        self.era = era
