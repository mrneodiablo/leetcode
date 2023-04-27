# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs_level_order(node, level):
            nonlocal ans
            if not node:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            dfs_level_order(node.left, level+1)
            dfs_level_order(node.right, level+1)

        dfs_level_order(root, 0)
        for i in range(len(ans)):
            if i & 1:
                ans[i] = ans[i][::-1]
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        expect = [[3], [20, 9], [15, 7]]
        self.assertEqual(
            str(self.solution.zigzagLevelOrder(root)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
