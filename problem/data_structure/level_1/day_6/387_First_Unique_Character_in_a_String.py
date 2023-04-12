import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "leetcode"
        expect = 0
        self.assertEqual(
            str(self.solution.firstUniqChar(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        s = "loveleetcode"
        expect = 2
        self.assertEqual(
            str(self.solution.firstUniqChar(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        # test case
        s = "aabb"
        expect = -1
        self.assertEqual(
            str(self.solution.firstUniqChar(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
