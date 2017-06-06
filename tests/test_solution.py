from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic1 = {1: 10, 2: 20, 3: 30, 4: 40}
        res = solution(dic1)

        self.assertEqual(res[0], (1, 10))
        self.assertEqual(res[1], (2, 20))
        self.assertEqual(res[2], (3, 30))
        self.assertEqual(res[3], (4, 40))
