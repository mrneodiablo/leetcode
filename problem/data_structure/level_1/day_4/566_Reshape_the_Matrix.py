from itertools import chain
from typing import List
import unittest


class Solution:
    def matrixReshape(self,
                      mat: List[List[int]],
                      r: int,
                      c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        out = []
        list1 = list(chain.from_iterable(mat))
        for i in range(0, len(list1), c):
            out.append(list1[i:i+c])
        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        mat = [[1, 2], [3, 4]]
        r = 1
        c = 4
        expect = [[1, 2, 3, 4]]
        self.assertEqual(
            str(self.solution.matrixReshape(mat, r, c)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        mat = [[1, 2], [3, 4]]
        r = 2
        c = 4
        expect = [[1, 2], [3, 4]]
        self.assertEqual(
            str(self.solution.matrixReshape(mat, r, c)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
