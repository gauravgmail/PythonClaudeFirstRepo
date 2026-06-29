import unittest
from sum_calculator import add_numbers


class TestSumCalculator(unittest.TestCase):
    """Unit tests for the sum calculator program."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_numbers(5, 3), 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(add_numbers(10, -5), 5)

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        self.assertEqual(add_numbers(-10, 5), -5)

    def test_add_with_zero(self):
        """Test adding a number with zero."""
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 5), 5)

    def test_add_two_zeros(self):
        """Test adding two zeros."""
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_floats(self):
        """Test adding two float numbers."""
        self.assertAlmostEqual(add_numbers(2.5, 3.7), 6.2)

    def test_add_float_and_integer(self):
        """Test adding float and integer."""
        self.assertEqual(add_numbers(5.5, 2), 7.5)

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)

    def test_add_negative_floats(self):
        """Test adding negative float numbers."""
        self.assertAlmostEqual(add_numbers(-2.5, -3.7), -6.2)


if __name__ == "__main__":
    unittest.main()
