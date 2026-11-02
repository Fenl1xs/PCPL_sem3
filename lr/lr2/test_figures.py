import math
import unittest

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.color import FigureColor


class TestFigures(unittest.TestCase):
    def test_figure_color_property(self):
        fc = FigureColor("синий")
        self.assertEqual(fc.color, "синий")
        fc.color = "желтый"
        self.assertEqual(fc.color, "желтый")

    def test_rectangle_area_and_repr(self):
        rect = Rectangle(width=4, height=5, color="синий")
        self.assertEqual(rect.area(), 20.0)
        self.assertEqual(rect.get_figure_name(), "Прямоугольник")
        self.assertIn("20.00", repr(rect))

    def test_circle_area(self):
        circ = Circle(radius=3, color="зеленый")
        expected_area = math.pi * 9
        self.assertAlmostEqual(circ.area(), expected_area, places=5)
        self.assertEqual(circ.get_figure_name(), "Круг")

    def test_square_inheritance_and_area(self):
        sq = Square(side=4, color="красный")
        self.assertIsInstance(sq, Rectangle)
        self.assertEqual(sq.area(), 16.0)
        self.assertEqual(sq.get_figure_name(), "Квадрат")


if __name__ == "__main__":
    unittest.main()