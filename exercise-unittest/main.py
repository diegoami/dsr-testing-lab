import unittest

# unittest docs
# https://docs.python.org/2/library/unittest.html

# assert docs
# https://docs.python.org/2/library/unittest.html#assert-methods

class TestIndex(unittest.TestCase):

    # Run before each test
    def setUp(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.repeating_string = "abababab"

    def test_my_first_test(self):
        self.assertEqual(self.alphabet.index('ab'), 0)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.alphabet.index('not_in_the_alphabet')

    # Run after each test
    def tearDown(self):
        return

if __name__ == '__main__':
    unittest.main()
