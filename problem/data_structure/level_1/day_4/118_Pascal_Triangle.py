from typing import List
import unittest


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            if i == 0:
                out.append([1])
            elif i == 1:
                out.append([1, 1])
            else:
                tmp = []
                for z in range(i+1):
                    if z == 0:
                        tmp.append(1)
                    elif z == i:
                        tmp.append(1)
                    else:
                        tmp.append(out[i-1][z-1]+out[i-1][z])
                out.append(tmp)
        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        numRows = 5
        expect = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(
            str(self.solution.generate(numRows)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        numRows = 1
        expect = [[1]]
        self.assertEqual(
            str(self.solution.generate(numRows)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
