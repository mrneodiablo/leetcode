from typing import List
import unittest


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            # compute the i-th element of the current row
            element = row[-1] * (rowIndex-i+1) // i
            row.append(element)
        return row


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        rowIndex = 3
        expect = [1, 3, 3, 1]
        self.assertEqual(
            str(self.solution.getRow(rowIndex)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        rowIndex = 1
        expect = [1, 1]
        self.assertEqual(
            str(self.solution.getRow(rowIndex)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
