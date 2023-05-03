# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        self.in_order_traversal(root, self.queue)

    def in_order_traversal(self, root, queue):
        if root:
            self.in_order_traversal(root.left, queue)
            queue.append(root.val)
            self.in_order_traversal(root.right, queue)

    def next(self) -> int:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return len(self.queue) != 0


class TestFunctions(unittest.TestCase):
    def test_run_1(self):
        # test case
        root = TreeNode(7,
                        TreeNode(3),
                        TreeNode(15, left=TreeNode(9), right=TreeNode(20))
                        )
        obj = BSTIterator(root)
        obj.next()
        param_2 = obj.hasNext()
        expect = True
        self.assertEqual(
            str(param_2),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
