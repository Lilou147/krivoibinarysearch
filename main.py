import unittest

from do_bs import DoBs


class TestDoBs(unittest.TestCase):

    def setUp(self):
        self.dobs = DoBs()

    def test_bs1(self):
        self.assertEqual(self.dobs.bs([1, 2, 3, 4, 5, 6], 3), (2, ''))

    def test_bs2(self):
        self.assertEqual(self.dobs.bs([11, 2, 14, 5, 7, 1], 5), (0, 'error'))

    def test_bs3(self):
        self.assertEqual(self.dobs.bs([-1, 12, 23, 34, 45, 56], -1), (0, ''))

    def test_bs4(self):
        self.assertEqual(self.dobs.bs([1, 11, 15, 34, 65, 771], 4), (0, 'not found'))


if __name__ == "__main__":
    unittest.main()
