from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                summ = nums[i]+nums[j]+nums[k]
                if summ == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j = j+1
                    k = k-1
                elif summ > 0:
                    k = k-1
                elif summ < 0:
                    j = j+1

        return list(res)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [3, 0, -2, -1, 1, 2]
        expect = [(-2, -1, 3), (-1, 0, 1), (-2, 0, 2)]
        self.assertEqual(
            str(self.solution.threeSum(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
