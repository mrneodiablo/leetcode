from collections import Counter
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        pls_odd = False
        for v in count.values():
            if v % 2 == 0:
                ans += v
            else:
                if v > 1:
                    ans += v-1
                pls_odd = True

        return ans+1 if pls_odd else ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        prices = "abccccdd"
        expect = 7
        self.assertEqual(
            self.solution.longestPalindrome(prices),
            expect,
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        prices = "a"
        expect = 1
        self.assertEqual(
            self.solution.longestPalindrome(prices),
            expect,
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
