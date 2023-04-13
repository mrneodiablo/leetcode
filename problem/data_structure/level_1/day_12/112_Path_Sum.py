# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:  # leaf node
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) \
            or self.hasPathSum(root.right, targetSum - root.val)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            5,
            left=TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
            right=TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        )
        targetSum = 22
        expect = True
        self.assertEqual(str(self.solution.hasPathSum(root, targetSum)),
                         str(expect),
                         "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        root = TreeNode(
            1,
            left=TreeNode(2),
            right=None,
        )
        targetSum = 1
        expect = False
        self.assertEqual(str(self.solution.hasPathSum(root, targetSum)),
                         str(expect),
                         "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
