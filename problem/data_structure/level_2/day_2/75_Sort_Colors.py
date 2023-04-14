from typing import List
import unittest


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        couter sort
        """
        counts = [0, 0, 0]
        for i in nums:
            counts[i] += 1

        i = 0
        for k in range(3):
            while counts[k] > 0:
                nums[i] = k
                i += 1
                counts[k] -= 1

        return nums


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expect = [0, 0, 1, 1, 2, 2]
        self.assertEqual(
            str(self.solution.sortColors(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
