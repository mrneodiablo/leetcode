# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        inorder = []

        def dfs(node):
            if not (node):
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        return inorder[k-1]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(3,
                        TreeNode(1, right=TreeNode(2)),
                        TreeNode(4)
                        )
        k = 1
        expect = 1
        self.assertEqual(
            str(self.solution.kthSmallest(root, k)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        root = TreeNode(5,
                        TreeNode(3, left=TreeNode(
                            2, left=TreeNode(1)), right=TreeNode(4)),
                        TreeNode(6)
                        )
        k = 3
        expect = 3
        self.assertEqual(
            str(self.solution.kthSmallest(root, k)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
