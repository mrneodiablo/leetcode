from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(root):
            if root:
                output.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return output


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            1,
            left=None,
            right=TreeNode(2, TreeNode(3, None, None), None)
        )
        expect = [1, 2, 3]
        self.assertEqual(str(self.solution.preorderTraversal(root)),
                         str(expect),
                         "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
