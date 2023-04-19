import unittest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split(" ")
        tmp = []
        if len(s) != len(pattern):
            return False

        for i, p in enumerate(pattern):
            if dic.get(p) is None and s[i] not in tmp:
                dic[p] = s[i]
                tmp.append(s[i])
            else:
                if dic.get(p) != s[i]:
                    return False

        return True


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        pattern = "abba"
        s = "dog cat cat dog"
        expect = True
        self.assertEqual(
            str(self.solution.wordPattern(pattern, s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        pattern = "abba"
        s = "dog cat cat fish"
        expect = False
        self.assertEqual(
            str(self.solution.wordPattern(pattern, s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
