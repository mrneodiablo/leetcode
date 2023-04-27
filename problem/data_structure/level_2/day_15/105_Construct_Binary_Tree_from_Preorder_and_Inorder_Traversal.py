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
    def buildTree(
            self,
            preorder: List[int],
            inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {k: v for v, k in enumerate(inorder)}
        preorder_index = 0

        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value]-1)
            root.right = array_to_tree(inorder_index_map[root_value]+1, right)

            return root

        return array_to_tree(0, len(inorder)-1)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expect = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))

        self.assertEqual(
            str(preorderTraversal(self.solution.buildTree(preorder, inorder))),
            str(preorderTraversal(expect)),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
