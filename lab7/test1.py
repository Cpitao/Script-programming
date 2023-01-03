from zad1 import *
from unittest import main, TestCase
import sys
import io


class Test_decorator(TestCase):

    def test_sum_3_args(self):
        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s
        
        op = Operacje()
        op.suma(1, 2, 3)
        self.assertEqual(s.getvalue(), "1+2+3=6\n")

        sys.stdout = old_stdout

    def test_sum_2_args(self):
        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s
        
        op = Operacje()
        op.suma(1, 2)
        self.assertEqual(s.getvalue(), "1+2+4=7\n")

        sys.stdout = old_stdout

    def test_sum_1_args(self):
        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s
        
        op = Operacje()
        op.suma(1)
        self.assertEqual(s.getvalue(), "1+4+5=10\n")

        sys.stdout = old_stdout

    def test_sum_0_args(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op.suma()
    
    def test_sub_2_args(self):
        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s
        
        op = Operacje()
        op.roznica(2, 1)
        self.assertEqual(s.getvalue(), "2-1=1\n")

        sys.stdout = old_stdout
    
    def test_sub_1_args(self):
        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s
        
        op = Operacje()
        op.roznica(2)
        self.assertEqual(s.getvalue(), "2-4=-2\n")

        sys.stdout = old_stdout
    
    def test_sub_0_args(self):
        op = Operacje()
        self.assertEqual(op.roznica(), 6)


class Test_settingitems(TestCase):
    def test_setitem(self):
        op = Operacje()
        op['suma'] = [1, 2]
        op['roznica'] = [1, 2, 3]

        old_stdout = sys.stdout
        s = io.StringIO()
        sys.stdout = s

        op.suma(1)
        self.assertEqual(s.getvalue(), "1+1+2=4\n")
        self.assertEqual(op.roznica(), 3)
        sys.stdout = old_stdout
    

if __name__ == "__main__":
    main()