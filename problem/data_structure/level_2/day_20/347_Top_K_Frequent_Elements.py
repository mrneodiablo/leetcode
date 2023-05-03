from collections import Counter
from typing import List
import unittest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        nums = sorted([[k, sequent] for k, sequent in count.items()],
                      key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans.append(nums[i][0])

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expect = [1, 2]
        self.assertEqual(
            str(self.solution.topKFrequent(nums, k)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        nums = [1]
        k = 1
        expect = [1]
        self.assertEqual(
            str(self.solution.topKFrequent(nums, k)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
