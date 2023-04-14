from typing import Counter, List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v == 1:
                return k
        return 0


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [2, 2, 1]
        expect = 1
        self.assertEqual(
            str(self.solution.singleNumber(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums = [4, 1, 2, 1, 2]
        expect = 4
        self.assertEqual(
            str(self.solution.singleNumber(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
