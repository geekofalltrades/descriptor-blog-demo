"""Step 7: We refactor the BoundedValue so that it restricts its value
to between arbitrary upper and lower bounds.
"""

Black = False
White = True


def bounded_value_factory(name, lower, upper):
    """Factory function for BoundedValues. Creates BoundedValues which
    store their data in the named attribute on the instance in which
    they're accessed.
    """

    class BoundedValue(object):
        """A value constrained to between given lower and upper bounds,
        inclusive.
        """

        def __init__(self, name, lower, upper):
            self.name = name
            self.lower = lower
            self.upper = upper

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            if value < self.lower or value > self.upper:
                raise ValueError(
                    "value must be between {} and {}, inclusive".format(
                        self.lower,
                        self.upper
                    )
                )

            setattr(instance, self.name, value)

    return BoundedValue(name, lower, upper)


class Piece(object):
    """A chess piece. Knows its color and location on the board."""

    rank = bounded_value_factory('_rank', 0, 8)
    file = bounded_value_factory('_file', 0, 8)
    stratum = bounded_value_factory('_stratum', 0, 8)
    era = bounded_value_factory('_era', -8, 8)

    def __init__(self, color, rank=0, file=0, stratum=0, era=0):
        self.color = color
        self.rank = rank
        self.file = file
        self.stratum = stratum
        self.era = era
