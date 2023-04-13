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
    def insertIntoBST(self,
                      root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        cur, next = None, root
        while next:
            cur = next
            if val < cur.val:
                next = cur.left
            elif val > cur.val:
                next = cur.right

        if val < cur.val:
            cur.left = TreeNode(val)
        else:
            cur.right = TreeNode(val)

        return root


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
        val = 5
        expect = [4, 2, 1, 3, 7, 5]
        self.assertEqual(
            str(preorderTraversal(self.solution.insertIntoBST(root, val))),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
