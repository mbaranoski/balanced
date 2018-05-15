import unittest
from balanced import balanced



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(balanced('abcd'), True)

    def test_something1(self):
        self.assertEqual(balanced('}abcd'), False)


if __name__ == '__main__':
    unittest.main()
