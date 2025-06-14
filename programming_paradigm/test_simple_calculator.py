import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_add(self):
        """
        Test the add method with various numerical inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.add(100, -50), 50, "Should be 50")
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "Should be 6.0 for floats")
        self.assertEqual(self.calc.add(-10, -5), -15, "Should be -15")

    def test_subtract(self):
        """
        Test the subtract method with various numerical inputs.
        """
        self.assertEqual(self.calc.subtract(5, 2), 3, "Should be 3")
        self.assertEqual(self.calc.subtract(2, 5), -3, "Should be -3")
        self.assertEqual(self.calc.subtract(10, 0), 10, "Should be 10")
        self.assertEqual(self.calc.subtract(0, 10), -10, "Should be -10")
        self.assertEqual(self.calc.subtract(-5, -2), -3, "Should be -3")
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0, "Should be 5.0 for floats")
        self.assertEqual(self.calc.subtract(-10, 5), -15, "Should be -15")

    def test_multiply(self):
        """
        Test the multiply method with various numerical inputs, including zero and negative numbers.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "Should be -6")
        self.assertEqual(self.calc.multiply(2, -3), -6, "Should be -6")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Should be 0 when multiplying by zero")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Should be 0 when multiplying zero by a number")
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0, "Should be 5.0 for floats")

    def test_divide(self):
        """
        Test the divide method, including normal division and division by zero.
        """
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Should be 2.0")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")
        self.assertEqual(self.calc.divide(-6, 3), -2.0, "Should be -2.0")
        self.assertEqual(self.calc.divide(6, -3), -2.0, "Should be -2.0")
        self.assertEqual(self.calc.divide(-6, -3), 2.0, "Should be 2.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "Should be 0.0 when numerator is zero")
        
        # Test division by zero, which should return None as per the SimpleCalculator's definition
        self.assertIsNone(self.calc.divide(10, 0), "Should return None for division by zero")
        self.assertIsNone(self.calc.divide(0, 0), "Should return None for 0/0")


if __name__ == '__main__':
    unittest.main()

