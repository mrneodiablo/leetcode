from math import inf
from typing import List
import unittest


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float(-inf), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        expect = 1
        self.assertEqual(
            str(self.solution.eraseOverlapIntervals(intervals)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        intervals = [[1, 2], [1, 2], [1, 2]]
        expect = 2
        self.assertEqual(
            str(self.solution.eraseOverlapIntervals(intervals)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
