# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = set()

        def dfs(node, seen):
            nonlocal k
            if not node:
                return False

            if (k - node.val) in seen:
                return True

            seen.add(node.val)

            return dfs(node.left, seen) or dfs(node.right, seen)

        return dfs(root, stack)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            5,
            left=TreeNode(3, TreeNode(2), TreeNode(4)),
            right=TreeNode(6, None, TreeNode(7)),
        )
        k = 9
        expect = True
        self.assertEqual(str(self.solution.findTarget(root, k)),
                         str(expect),
                         "incorrect, expect is " + str(expect))

    # def test_run_2(self):
    #     # test case
    #     root = TreeNode(
    #         5,
    #         left=TreeNode(3,TreeNode(2),TreeNode(4)),
    #         right=TreeNode(6,None,TreeNode(7)),
    #     )
    #     k = 28
    #     expect = True
    #     self.assertEqual(str(self.solution.findTarget(root,k)),
    #                      str(expect),
    #                      "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
