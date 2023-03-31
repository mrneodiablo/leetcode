from typing import List
import unittest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(list(set(nums))) != len(nums):
            return True
        return False


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [1, 2, 3, 1]
        expect = True
        self.assertEqual(
            str(self.solution.containsDuplicate(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        nums = [1, 2, 3, 4]
        expect = False
        self.assertEqual(
            str(self.solution.containsDuplicate(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expect = True
        self.assertEqual(
            str(self.solution.containsDuplicate(nums)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
