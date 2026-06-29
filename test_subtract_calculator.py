import unittest
from subtract_calculator import subtract_numbers


class TestSubtractCalculator(unittest.TestCase):
    """Unit tests for the subtract calculator program."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        self.assertEqual(subtract_numbers(10, 3), 7)

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        self.assertEqual(subtract_numbers(-5, -3), -2)

    def test_subtract_positive_from_negative(self):
        """Test subtracting positive from negative number."""
        self.assertEqual(subtract_numbers(-10, 5), -15)

    def test_subtract_negative_from_positive(self):
        """Test subtracting negative from positive number."""
        self.assertEqual(subtract_numbers(10, -5), 15)

    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        self.assertEqual(subtract_numbers(5, 0), 5)
        self.assertEqual(subtract_numbers(0, 5), -5)

    def test_subtract_two_zeros(self):
        """Test subtracting two zeros."""
        self.assertEqual(subtract_numbers(0, 0), 0)

    def test_subtract_floats(self):
        """Test subtracting two float numbers."""
        self.assertAlmostEqual(subtract_numbers(7.5, 2.3), 5.2)

    def test_subtract_float_and_integer(self):
        """Test subtracting float and integer."""
        self.assertEqual(subtract_numbers(5.5, 2), 3.5)

    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        self.assertEqual(subtract_numbers(5000000, 2000000), 3000000)

    def test_subtract_negative_floats(self):
        """Test subtracting negative float numbers."""
        self.assertAlmostEqual(subtract_numbers(-5.5, -2.3), -3.2)

    def test_subtract_same_numbers(self):
        """Test subtracting identical numbers."""
        self.assertEqual(subtract_numbers(42, 42), 0)


if __name__ == "__main__":
    unittest.main()
