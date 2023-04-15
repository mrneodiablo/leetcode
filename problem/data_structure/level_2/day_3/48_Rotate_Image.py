from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:

            for i in range(r-l):
                top, bottom = l, r

                topLeft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom - i][l]

                matrix[bottom-i][l] = matrix[bottom][r-i]

                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topLeft

            r -= 1
            l += 1
        return matrix


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expect = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(
            str(self.solution.rotate(matrix)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10],
                  [13, 3, 6, 7], [15, 14, 12, 16]]
        expect = [[15, 13, 2, 5], [14, 3, 4, 1],
                  [12, 6, 8, 9], [16, 7, 10, 11]]
        self.assertEqual(
            str(self.solution.rotate(matrix)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
