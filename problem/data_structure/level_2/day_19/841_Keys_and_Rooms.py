from typing import List
import unittest


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can_visit = set()

        def dfs(key):
            if key in can_visit:
                return
            can_visit.add(key)
            for k in rooms[key]:
                dfs(k)

        dfs(0)
        return len(can_visit) == len(rooms)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        rooms = [[1], [2], [3], []]
        expect = True
        self.assertEqual(
            str(self.solution.canVisitAllRooms(rooms)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        expect = False
        self.assertEqual(
            str(self.solution.canVisitAllRooms(rooms)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
