from typing import List
import unittest


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n > second:
                return True

            if n > first:
                second = min(n, second)
            else:
                first = min(n, first)
        return False


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        nums = [20, 100, 10, 12, 5, 13]
        expect = True
        self.assertEqual(
            str(self.solution.increasingTriplet(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
