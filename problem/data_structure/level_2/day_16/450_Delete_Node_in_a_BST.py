# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = []

    def dfs(root):
        if root:
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)

    dfs(root)
    return output


class Solution:
    def deleteNode(self,
                   root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            if root.left and root.right:
                node = root.left
                while node.right:
                    node = node.right
                # The value of the inorder successor is copied to the root
                root.val = node.val
                # The inorder successor is then deleted
                # from the right subtree of the root
                root.left = self.deleteNode(root.left, node.val)

        return root


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(5,
                        TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
                        TreeNode(6, left=None, right=TreeNode(7))
                        )
        key = 3
        expect = [2, 4, 5, 6, 7]
        self.assertEqual(
            str(inorderTraversal(self.solution.deleteNode(root, key))),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
