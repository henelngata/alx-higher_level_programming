import unittest
from models.rectangle import Rectangle
from models.base import Base
class TestRectangle(unittest.TestCase):
    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))
    def test_constructor(self):
        # Test instance creation with default values
        rect1 = Rectangle(10, 20)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 20)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        # Test instance creation with custom values
        rect2 = Rectangle(5, 8, 2, 3)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 8)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 3)

    def test_properties(self):
        rect = Rectangle(10, 20)
        rect.width = 15
        rect.height = 25
        rect.x = 3
        rect.y = 5

        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)
    
    def test_width_property(self):
        rect = Rectangle(10, 20)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_property(self):
        rect = Rectangle(10, 20)
        rect.height = 25
        self.assertEqual(rect.height, 25)

    def test_x_property(self):
        rect = Rectangle(10, 20)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y_property(self):
        rect = Rectangle(10, 20)
        rect.y = 5
        self.assertEqual(rect.y, 5)
if __name__ == '__main__':
    unittest.main()
