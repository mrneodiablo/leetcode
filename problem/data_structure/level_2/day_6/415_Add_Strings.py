import unittest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if (len(num1) - len(num2)) > 0:
            num2 = '0'*(len(num1) - len(num2)) + num2
        else:
            num1 = '0'*(len(num2) - len(num1)) + num1

        out = ""
        carry = 0
        while len(num1) > 0:

            last_num1 = num1[-1]
            last_num2 = num2[-1]

            sum = int(last_num1) + int(last_num2) + carry
            carry = sum//10
            out = str(sum % 10) + out

            num1 = num1[:-1]
            num2 = num2[:-1]

        if carry == 1:
            out = "1" + out

        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        num1 = "11"
        num2 = "123"
        expect = "134"
        self.assertEqual(
            str(self.solution.addStrings(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        num1 = "456"
        num2 = "77"
        expect = "533"
        self.assertEqual(
            str(self.solution.addStrings(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
