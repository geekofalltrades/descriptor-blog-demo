import unittest
from piece import Piece, Black, White


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


if __name__ == '__main__':
    unittest.main()
