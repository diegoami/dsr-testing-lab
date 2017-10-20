import unittest

# unittest docs
# https://docs.python.org/2/library/unittest.html

# assert docs
# https://docs.python.org/2/library/unittest.html#assert-methods

# string.index docs
# https://docs.python.org/2/library/string.html#string.index

class TestIndex(unittest.TestCase):

    # Run before each test
    def setUp(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.repeating_string = "abababab"
        self.diego_string = "My Name is Diego and again Diego"

    def test_alphabet_test(self):
        self.assertEqual(self.alphabet.index('ab'), 0)



    def test_repeating_2_test(self):
        self.assertEqual(self.repeating_string.index('ab',1 ), 2)


    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.alphabet.index('not_in_the_alphabet')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.alphabet.index('not_in_the_alphabet')


    def test_diego_1(self):
        self.assertEqual(self.diego_string.index('Diego'),11)

    def test_diego_2(self):
        self.assertEqual(self.diego_string.index( 'Diego', 12), 27)

    def test_diego_3(self):
        with self.assertRaises(ValueError):
            self.diego_string.index( 'Diego', 0, 3)

    # Run after each test
    def tearDown(self):
        return

if __name__ == '__main__':
    unittest.main()
