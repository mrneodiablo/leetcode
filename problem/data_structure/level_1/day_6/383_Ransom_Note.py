from collections import Counter
import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(list(magazine)) >= Counter(list(ransomNote))


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        ransomNote = "a"
        magazine = "b"
        expect = False
        self.assertEqual(
            str(self.solution.canConstruct(ransomNote, magazine)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        ransomNote = "aa"
        magazine = "ab"
        expect = False
        self.assertEqual(
            str(self.solution.canConstruct(ransomNote, magazine)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        # test case
        ransomNote = "aa"
        magazine = "aab"
        expect = True
        self.assertEqual(
            str(self.solution.canConstruct(ransomNote, magazine)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
