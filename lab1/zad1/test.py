from fractions import Fraction
from multiprocessing.sharedctypes import Value
import main
import unittest


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)
        
    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(TypeError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(1, 2), Fraction(2, 3)), Fraction(7, 6))

    def test_sum_nan_types(self):
        with self.assertRaises(TypeError):
            main.sum(1, [1, 2])



if __name__ == "__main__":
    unittest.main()