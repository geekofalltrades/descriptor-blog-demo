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


if __name__ == '__main__':
    unittest.main()
