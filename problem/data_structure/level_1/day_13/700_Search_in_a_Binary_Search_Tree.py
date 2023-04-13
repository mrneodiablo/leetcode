# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = []

    def dfs(root):
        if root:
            output.append(root.val)
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return output


class Solution:
    def searchBST(self,
                  root: Optional[TreeNode],
                  val: int) -> Optional[TreeNode]:
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            4,
            left=TreeNode(2, TreeNode(1), TreeNode(3)),
            right=TreeNode(7),
        )
        val = 2
        expect = [2, 1, 3]
        self.assertEqual(
            str(preorderTraversal(self.solution.searchBST(root, val))
                ), str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        root = TreeNode(
            4,
            left=TreeNode(2, TreeNode(1), TreeNode(3)),
            right=TreeNode(7),
        )
        val = 5
        expect = []
        self.assertEqual(
            str(preorderTraversal(self.solution.searchBST(root, val))),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
