# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(root, level):
            nonlocal max_depth
            if root:
                level += 1
                max_depth = max(max_depth, level)
                dfs(root.left, level)
                dfs(root.right, level)

        dfs(root, 0)
        return max_depth


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20,
                           TreeNode(15, None, None),
                           TreeNode(7, None, None))
        )
        expect = 3
        self.assertEqual(str(self.solution.maxDepth(root)),
                         str(expect),
                         "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
