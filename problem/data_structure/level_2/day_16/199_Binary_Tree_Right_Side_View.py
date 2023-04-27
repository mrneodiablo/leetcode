# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs_level(node, level):
            nonlocal ans
            if not node:
                return

            if level == len(ans):
                ans.append(node.val)

            dfs_level(node.right, level+1)
            dfs_level(node.left, level+1)

        dfs_level(root, 0)
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(
            3, left=None, right=TreeNode(4)))
        expect = [1, 3, 4]
        self.assertEqual(
            str(self.solution.rightSideView(root)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
