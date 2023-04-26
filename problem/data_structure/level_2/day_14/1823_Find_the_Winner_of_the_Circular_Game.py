import unittest


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n + 1))
        tmp = 0
        while len(players) > 1:
            if tmp == (k - 1):
                players.pop(0)
                tmp = 0
                continue

            first = players.pop(0)
            players.append(first)
            tmp += 1
        return players[0]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        n = 5
        k = 2
        expect = 3
        self.assertEqual(self.solution.findTheWinner(n, k),
                         expect,
                         "incorrect, expect is " + str(expect)
                         )

    def test_run_2(self):
        # test case
        n = 6
        k = 5
        expect = 1
        self.assertEqual(self.solution.findTheWinner(n, k),
                         expect,
                         "incorrect, expect is " + str(expect)
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
