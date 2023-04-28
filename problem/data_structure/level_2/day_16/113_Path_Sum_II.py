# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node: Optional[TreeNode], path) -> None:
            nonlocal ans
            if not node:
                return

            if (not node.left) and (not node.right):  # left node
                path.append(node.val)
                if targetSum == sum(path):
                    ans.append(path)

            dfs(node.left, path+[node.val])
            dfs(node.right, path+[node.val])

        dfs(root, [])
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(5,
                        TreeNode(4, left=TreeNode(
                            11, left=TreeNode(7), right=TreeNode(2))),
                        TreeNode(8, left=TreeNode(13), right=TreeNode(
                            4, left=TreeNode(5), right=TreeNode(1)))
                        )
        targetSum = 22
        expect = [[5, 4, 11, 2], [5, 8, 4, 5]]
        self.assertEqual(
            str(self.solution.pathSum(root, targetSum)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
