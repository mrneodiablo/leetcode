from typing import List
import unittest


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[n*n]*n for i in range(n)]
        l, r = 0, n - 1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                if l+i-1 >= 0:
                    ans[top][l+i] = ans[top][l+i-1]+1
                else:
                    ans[top][l+i] = i+1

                ans[top+i][r] = ans[top][l+i] + (r-l)

                ans[bottom][r-i] = ans[top+i][r] + (r-l)
                ans[bottom-i][l] = ans[bottom][r-i] + (r-l)

            l += 1
            r -= 1
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        n = 3
        expect = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(
            str(self.solution.generateMatrix(n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        n = 1
        expect = [[1]]
        self.assertEqual(
            str(self.solution.generateMatrix(n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        # test case
        n = 4
        expect = [[1, 2, 3, 4], [12, 13, 14, 5],
                  [11, 16, 15, 6], [10, 9, 8, 7]]
        self.assertEqual(
            str(self.solution.generateMatrix(n)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
