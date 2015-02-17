import unittest
from piece import BoundedValue, Piece, Black, White


class TestBoundedValue(unittest.TestCase):
    class BoundedValueTestClass(object):
        """A simple object with a BoundedValue for testing."""
        value = BoundedValue()

    def setUp(self):
        self.obj = self.BoundedValueTestClass()

    def test_multiple_instances(self):
        """Multiple instances with the same descriptor have their
        own values.
        """
        other = self.BoundedValueTestClass()
        self.obj.value = 4
        other.value = 2
        self.assertEqual(self.obj.value, 4)
        self.assertEqual(other.value, 2)

    def test_valid_values(self):
        """BoundedValue may be assigned values in the 0-8 range."""
        for value in range(9):
            try:
                self.obj.value = value
            except ValueError:
                raise AssertionError(
                    "self.obj.value could not be assigned the value"
                    " {}".format(value)
                )

    def test_invalid_values(self):
        """BoundedValue may not be assigned values outside the 0-8 range."""
        with self.assertRaises(ValueError):
            self.obj.value = -1

        with self.assertRaises(ValueError):
            self.obj.value = 9


class TestPiece(unittest.TestCase):
    def test_init_defaults(self):
        """Pieces are initialized with expected defaults."""
        for color in (Black, White):
            p = Piece(color)
            self.assertTrue(p.color is color)
            self.assertEqual(p.rank, 0)
            self.assertEqual(p.file, 0)

    def test_init_values(self):
        """Pieces are assigned expected values on creation."""
        p = Piece(Black, 2, 4)
        self.assertTrue(p.color is Black)
        self.assertEqual(p.rank, 2)
        self.assertEqual(p.file, 4)

    # All tests below this point are now redundant and can be removed -
    # they're retesting BoundedValue. However, they're left in place to
    # demonstrate that they still pass.

    def test_valid_ranks(self):
        """Pieces may be assigned ranks in the 0-8 range."""
        p = Piece(Black)
        for rank in range(9):
            try:
                p.rank = rank
            except ValueError:
                raise AssertionError(
                    "Piece.rank could not be assigned the value"
                    " {}".format(rank)
                )

    def test_valid_files(self):
        """Pieces may be assigned files in the 0-8 range."""
        p = Piece(Black)
        for file in range(9):
            try:
                p.file = file
            except ValueError:
                raise AssertionError(
                    "Piece.file could not be assigned the value"
                    " {}".format(file)
                )

    def test_valid_strata(self):
        """Pieces may be assigned strata in the 0-8 range."""
        p = Piece(Black)
        for stratum in range(9):
            try:
                p.stratum = stratum
            except ValueError:
                raise AssertionError(
                    "Piece.stratum could not be assigned the value"
                    " {}".format(stratum)
                )

    def test_valid_eras(self):
        """Pieces may be assigned eras in the 0-8 range."""
        p = Piece(Black)
        for era in range(9):
            try:
                p.era = era
            except ValueError:
                raise AssertionError(
                    "Piece.era could not be assigned the value"
                    " {}".format(era)
                )

    def test_invalid_ranks(self):
        """Pieces may not be assigned ranks outside the 0-8 range."""
        p = Piece(Black)

        with self.assertRaises(ValueError):
            p.rank = -1

        with self.assertRaises(ValueError):
            p.rank = 9

    def test_invalid_files(self):
        """Pieces may not be assigned files outside the 0-8 range."""
        p = Piece(Black)

        with self.assertRaises(ValueError):
            p.file = -1

        with self.assertRaises(ValueError):
            p.file = 9

    def test_invalid_strata(self):
        """Pieces may not be assigned strata outside the 0-8 range."""
        p = Piece(Black)

        with self.assertRaises(ValueError):
            p.stratum = -1

        with self.assertRaises(ValueError):
            p.stratum = 9

    def test_invalid_eras(self):
        """Pieces may not be assigned eras outside the 0-8 range."""
        p = Piece(Black)

        with self.assertRaises(ValueError):
            p.era = -1

        with self.assertRaises(ValueError):
            p.era = 9


if __name__ == '__main__':
    unittest.main()
