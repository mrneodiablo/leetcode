import unittest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, st in enumerate(s):
            if st == "(":
                stack.append(i)
            elif st == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''

        return "".join(s)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "lee(t(c)o)de)"
        expect = "lee(t(c)o)de"
        self.assertEqual(self.solution.minRemoveToMakeValid(s),
                         expect,
                         "incorrect, expect is " + str(expect)
                         )

    def test_run_2(self):
        # test case
        s = "a)b(c)d"
        expect = "ab(c)d"
        self.assertEqual(self.solution.minRemoveToMakeValid(s),
                         expect,
                         "incorrect, expect is " + str(expect)
                         )

    def test_run_3(self):
        # test case
        s = "))(("
        expect = ""
        self.assertEqual(self.solution.minRemoveToMakeValid(s),
                         expect,
                         "incorrect, expect is " + str(expect)
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
