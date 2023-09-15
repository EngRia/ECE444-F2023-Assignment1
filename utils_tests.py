from utils import utils
import unittest

class test_code(unittest.TestCase):
    def test_reversed(self):
        ans_rev = utils().reversed(987)
        self.assertEqual(ans_rev, 789)
        with self.assertRaises(TypeError):
            utils().reversed(7.8)
        with self.assertRaises(TypeError):
            utils().reversed('any word')

    def test_formatter(self):
        ans_bin, ans_oct = utils().formatter(50)
        self.assertEqual(ans_bin, '0b110010')
        self.assertEqual(ans_oct, '0o62')
        with self.assertRaises(TypeError):
            utils().reversed(90.8)
        with self.assertRaises(TypeError):
            utils().reversed('any word for this test too')

if __name__ == '__main__':
    unittest.main()
