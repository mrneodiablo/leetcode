import unittest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0
        for i, s in enumerate(num1):
            num1_int += (ord(s)-48)*1*10**(len(num1)-1-i)

        for i, s in enumerate(num2):
            num2_int += (ord(s)-48)*1*10**(len(num2)-1-i)

        return str(num1_int*num2_int)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        num1 = "2"
        num2 = "3"
        expect = "6"
        self.assertEqual(
            str(self.solution.multiply(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        num1 = "123"
        num2 = "456"
        expect = "56088"
        self.assertEqual(
            str(self.solution.multiply(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
