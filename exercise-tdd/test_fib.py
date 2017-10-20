from .main import fib
import unittest


class TestFibonacci(unittest.TestCase):
    def test_fib_0(self):
        self.assertEqual(fib(0), 0)


    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib(5), 5)

    def test_fib_6(self):
        self.assertEqual(fib(6), 8)

    def test_fib_7(self):
        self.assertEqual(fib(7), 13)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

 #   def test_fib_100(self):
  #      self.assertGreater(fib(100) > fib(99))


    def test_fib_min0 (self):
        with self.assertRaises(ValueError):
            fib(-1)


if __name__  == '__main__':
    unittest.main()


