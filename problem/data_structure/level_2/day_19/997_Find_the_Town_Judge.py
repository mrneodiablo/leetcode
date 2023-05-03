from typing import List
import unittest


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {i: [] for i in range(1, n+1)}
        trusteeMap = {i: [] for i in range(1, n+1)}

        for t in trust:
            trustMap[t[1]].append(t[0])
            trusteeMap[t[0]].append(t[1])

        for i, jList in trustMap.items():
            if len(jList) == (n - 1) and len(trusteeMap[i]) == 0:
                return i

        return -1


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        n = 4
        trust = [[1, 3], [1, 4], [2, 3]]
        expect = -1
        self.assertEqual(
            str(self.solution.findJudge(n, trust)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        n = 3
        trust = [[1, 3], [2, 3]]
        expect = 3
        self.assertEqual(
            str(self.solution.findJudge(n, trust)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_3(self):
        # test case
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        expect = 3
        self.assertEqual(
            str(self.solution.findJudge(n, trust)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
