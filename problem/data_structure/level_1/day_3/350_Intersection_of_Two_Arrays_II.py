from collections import Counter
from typing import List
import unittest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        counter_nums1 = Counter(nums1)
        counter_nums2 = Counter(nums2)

        for k, v in counter_nums1.items():
            if counter_nums2.get(k) is not None:
                out += [k for i in range(min(counter_nums2.get(k), v))]
        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expect = [2, 2]
        self.assertEqual(
            str(self.solution.intersect(nums1, nums2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expect = [4, 9]
        self.assertEqual(
            str(self.solution.intersect(nums1, nums2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
