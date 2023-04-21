import unittest


class Solution:
    def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        # filling the dp table
        for i in range(len(s)-1, -1, -1):
            # j starts from the i location :
            # to only work on the upper side of the diagonal
            for j in range(i+1, len(s)):
                if s[i] == s[j]:  # if the chars mathces
                    # if len slicied sub_string is just one letter
                    # if the characters are equal,
                    # we can say they are palindomr dp[i][j] =True
                    # if the slicied sub_string is
                    # longer than 1,
                    # then we should check if the inner string
                    # is also palindrom
                    # (check dp[i+1][j-1] is True)
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the
                        # maximum palindrom sequence
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]

        return longest_palindrom


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "babad"
        expect = "aba"
        self.assertEqual(
            str(self.solution.longestPalindrome(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        s = "cbbd"
        expect = "bb"
        self.assertEqual(
            str(self.solution.longestPalindrome(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
