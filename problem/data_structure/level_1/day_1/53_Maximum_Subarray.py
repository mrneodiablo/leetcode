from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp = max(temp, 0)
            temp += nums[i]
            if temp > max_sum:
                max_sum = temp
        return max_sum


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expect = 6
        self.assertEqual(
            str(self.solution.maxSubArray(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums = [1]
        expect = 1
        self.assertEqual(
            str(self.solution.maxSubArray(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        nums = [5, 4, -1, 7, 8]
        expect = 23
        self.assertEqual(
            str(self.solution.maxSubArray(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
