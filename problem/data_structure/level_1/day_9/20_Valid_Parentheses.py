import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) > 0:
                    if c == ")" and stack[-1] == "(":
                        stack.pop()
                    elif c == "}" and stack[-1] == "{":
                        stack.pop()
                    elif c == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        return True


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "()"
        expect = True
        self.assertEqual(str(self.solution.isValid(s)),
                         str(expect),
                         "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        s = "()[]{}"
        expect = True
        self.assertEqual(str(self.solution.isValid(s)),
                         str(expect),
                         "incorrect, expect is " + str(expect))

    def test_run_3(self):
        # test case
        s = "(]"
        expect = False
        self.assertEqual(str(self.solution.isValid(s)),
                         str(expect),
                         "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
