from typing import List
import unittest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums)//2)]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [3, 2, 3]
        expect = 3
        self.assertEqual(
            str(self.solution.majorityElement(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        expect = 2
        self.assertEqual(
            str(self.solution.majorityElement(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
