from typing import List
import unittest

# better and good solution
# class Solution(object):
#     def isValidSudoku(self, board):
#         res = []
#         for i in range(9):
#             for j in range(9):
#                 element = board[i][j]
#                 if element != '.':
#                     res += [
#                            (i, element),
#                            (element, j),
#                            (i // 3, j // 3, element)
#                       ]
#         return len(res) == len(set(res))

# my own solution


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != len(board[0]):
            return False

        # check straight line
        for row in board:
            checker = {}
            for value in row:
                if value != ".":
                    if checker.get(value) is not None:
                        return False
                    checker[value] = 1

        # check straight column
        for column in range(len(board[0])):
            checker = {}
            for row in range(len(board)):
                if board[row][column] != ".":
                    if checker.get(board[row][column]) is not None:
                        return False
                    checker[board[row][column]] = 1

        # check matrix 3x3
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                checker = {}
                values = board[i][j:j+3] + \
                    board[i+1][j:j+3] + board[i+2][j:j+3]
                for value in values:
                    if value != ".":
                        if checker.get(value) is not None:
                            return False
                        checker[value] = 1
        return True


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        expect = True
        self.assertEqual(
            str(self.solution.isValidSudoku(board)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        expect = False
        self.assertEqual(
            str(self.solution.isValidSudoku(board)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
