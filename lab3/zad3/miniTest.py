import unittest
from DeanerySystem.day import *
from DeanerySystem.term import *
from unittest import TestCase, main


class Test_Term(unittest.TestCase):

    def test_str(self):
        term = Term(Day.TUE, 9, 45)
        self.assertEqual(term.__str__(), "Wtorek 9:45 [90]")
    
    def test_eq_true(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.TUE, 9, 45)
        self.assertTrue(term1.equals(term2))
    
    def test_eq_false(self):
        term1 = Term(Day.TUE, 9, 30)
        term2 = Term(Day.WED, 9, 30)
        self.assertFalse(term1.equals(term2))

    def test_earlier(self):
        term1 = Term(Day.TUE, 9, 30)
        term2 = Term(Day.WED, 8, 30)
        self.assertTrue(term1.earlierThan(term2))
        self.assertFalse(term2.earlierThan(term1))
    
    def test_later(self):
        term1 = Term(Day.TUE, 9, 30)
        term2 = Term(Day.WED, 9, 30)
        self.assertTrue(term2.laterThan(term1))
        self.assertFalse(term1.laterThan(term2))


if __name__ == "__main__":
    unittest.main()
