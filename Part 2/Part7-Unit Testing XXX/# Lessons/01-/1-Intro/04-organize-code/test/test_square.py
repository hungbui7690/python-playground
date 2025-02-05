# The test_square module uses the Square and Shape classes from the square and shape modules in the shapes package.

import unittest

from shapes.square import Square
from shapes.shape import Shape


class TestSquare(unittest.TestCase):
    def test_create_square_negative_length(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_square_instance_of_shape(self):
        square = Square(10)
        self.assertIsInstance(square, Shape)

    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)
