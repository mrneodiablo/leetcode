from collections import Counter
import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(list(s)) == Counter(list(t))


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "anagram"
        t = "nagaram"
        expect = True
        self.assertEqual(
            str(self.solution.isAnagram(s, t)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        s = "rat"
        t = "car"
        expect = False
        self.assertEqual(
            str(self.solution.isAnagram(s, t)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
