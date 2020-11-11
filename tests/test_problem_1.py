import unittest

from solutions import problem_1


class Test(unittest.TestCase):
    def test_1(self):
        result = problem_1.determine_min_broadcast_range(
            [1, 5, 11, 20], [4, 8, 15])
        self.assertEqual(5, result)

    def test_2(self):
        result = problem_1.determine_min_broadcast_range_2(
            [1, 5, 11, 20], [4, 8, 15])
        self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()
