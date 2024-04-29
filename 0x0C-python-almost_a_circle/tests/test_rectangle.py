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

    def test_bad_constructor(self):
        # Test invalid width (non-integer)
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 0, 0)

        # Test invalid height (zero value)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0)

        # Test invalid x (negative value)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -2, 0)

        # Test invalid y (non-integer)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 0, "invalid")
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
    
    def test_width_property_with_invalid(self):
        rect = Rectangle(10, 20)
        # Test invalid width (non-integer)
        with self.assertRaises(TypeError):
            rect.width = "invalid"

        # Test invalid width (negative value)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_property(self):
        rect = Rectangle(10, 20)
        rect.height = 25
        self.assertEqual(rect.height, 25)
    
    def test_height_property_with_invalid(self):
        rect = Rectangle(10, 20)
        # Test invalid height (non-integer)
        with self.assertRaises(TypeError):
            rect.height = "invalid"

        # Test invalid height (zero value)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_property(self):
        rect = Rectangle(10, 20)
        rect.x = 3
        self.assertEqual(rect.x, 3)

        # Test invalid x (non-integer)
        with self.assertRaises(TypeError):
            rect.x = "invalid"

        # Test invalid x (negative value)
        with self.assertRaises(ValueError):
            rect.x = -2
    
    def test_y_property(self):
        rect = Rectangle(10, 20)
        rect.y = 5
        self.assertEqual(rect.y, 5)

        # Test invalid y (non-integer)
        with self.assertRaises(TypeError):
            rect.y = "invalid"

        # Test invalid y (negative value)
        with self.assertRaises(ValueError):
            rect.y = -3
if __name__ == '__main__':
    unittest.main()
