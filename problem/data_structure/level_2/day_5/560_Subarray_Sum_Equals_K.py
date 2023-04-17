from typing import List
import unittest


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        ansCount = 0
        prevSums = {0: 1}

        for num in nums:

            currSum += num

            if currSum - k in prevSums:
                ansCount += prevSums[currSum - k]

            if currSum in prevSums:
                prevSums[currSum] += 1
            else:
                prevSums[currSum] = 1

        return ansCount


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    # def test_run_1(self):
    #     # test case
    #     nums = [1,1,1]
    #     k = 2
    #     expect = 2
    #     self.assertEqual(
    #         str(self.solution.subarraySum(nums,k)),
    #         str(expect),
    #         "incorrect, expect is " + str(expect)
    #     )

    def test_run_2(self):
        # test case
        nums = [1, 2, 3]
        k = 3
        expect = 2
        self.assertEqual(
            str(self.solution.subarraySum(nums, k)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
