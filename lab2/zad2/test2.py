import unittest
from zad2 import get_tokens


class Test_print_tokens(unittest.TestCase):

    def test_string(self):
        line = "helloąęć nice txt!"
        correct = """String: helloąęć nice txt!"""
        self.assertEqual(correct, get_tokens(line))
    
    def test_number(self):
        line = "123 345 0123"
        correct = """Number: 123
Number: 345
Number: 0
Number: 123"""
        self.assertEqual(correct, get_tokens(line))

    def test_mixed(self):
        line = "hello 0123 there:)123"
        correct = """String: hello 
Number: 0
Number: 123
String:  there:)
Number: 123"""
        self.assertEqual(correct, get_tokens(line))


if __name__ == "__main__":
    unittest.main()