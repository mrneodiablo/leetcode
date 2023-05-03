import heapq
from typing import List
import unittest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap, res = [], 0
        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            res = -heapq.heappop(maxheap)
        return res


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expect = 5
        self.assertEqual(
            str(self.solution.findKthLargest(nums, k)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expect = 4
        self.assertEqual(
            str(self.solution.findKthLargest(nums, k)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
