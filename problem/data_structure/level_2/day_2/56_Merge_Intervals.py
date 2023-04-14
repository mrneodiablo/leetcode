from typing import List
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expect = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(
            str(self.solution.merge(intervals)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        intervals = [[1, 4], [4, 5]]
        expect = [[1, 5]]
        self.assertEqual(
            str(self.solution.merge(intervals)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        intervals = [[1, 4], [5, 6]]
        expect = [[1, 4], [5, 6]]
        self.assertEqual(
            str(self.solution.merge(intervals)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
