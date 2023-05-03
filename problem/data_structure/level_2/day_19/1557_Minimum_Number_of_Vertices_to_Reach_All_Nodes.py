from typing import List
import unittest


class Solution:
    def findSmallestSetOfVertices(self,
                                  n: int,
                                  edges: List[List[int]]
                                  ) -> List[int]:
        indegree = [0]*(n)
        for i, j in edges:
            indegree[j] += 1
        lst = []
        for i in range(n):
            if indegree[i] == 0:
                lst.append(i)
        return lst


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        n = 6
        edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        expect = [0, 3]
        self.assertEqual(
            str(self.solution.findSmallestSetOfVertices(n, edges)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        n = 5
        edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
        expect = [0, 2, 3]
        self.assertEqual(
            str(self.solution.findSmallestSetOfVertices(n, edges)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
