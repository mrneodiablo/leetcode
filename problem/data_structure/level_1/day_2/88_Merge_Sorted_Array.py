from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int],
              m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        expect = [1, 2, 2, 3, 5, 6]
        self.assertEqual(
            str(self.solution.merge(nums1, m, nums2, n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expect = [1]
        self.assertEqual(
            str(self.solution.merge(nums1, m, nums2, n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expect = [1]
        self.assertEqual(
            str(self.solution.merge(nums1, m, nums2, n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
