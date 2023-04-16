from typing import List
import unittest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0]) - 1
        row = 0

        while col >= 0 and row < len(matrix):
            if matrix[row][col] > target:
                col -= 1

            elif matrix[row][col] < target:
                row += 1

            else:
                return True

        return False


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
            3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 5
        expect = True
        self.assertEqual(
            str(self.solution.searchMatrix(matrix, target)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
            3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 20
        expect = False
        self.assertEqual(
            str(self.solution.searchMatrix(matrix, target)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
