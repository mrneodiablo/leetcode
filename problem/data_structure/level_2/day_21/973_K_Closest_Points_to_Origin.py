from math import sqrt
from typing import List
import unittest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        sort_points_by_distance = []
        for i, point in enumerate(points):
            distance = sqrt(point[0]**2 + point[1]**2)
            sort_points_by_distance.append([i, distance])

        sort_points_by_distance.sort(key=lambda x: x[1])
        for i in range(k):
            ans.append(points[sort_points_by_distance[i][0]])

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        expect = [[-2, 2]]
        self.assertEqual(
            str(self.solution.kClosest(points, k)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expect = [[3, 3], [-2, 4]]
        self.assertEqual(
            str(self.solution.kClosest(points, k)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
