# Definition for a binary tree node.
from collections import deque
import unittest


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"

        ans = str(root.val) + ","
        ans += self.serialize(root.left) + ","
        ans += self.serialize(root.right)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_helper(queue):
            val = queue.popleft()
            if val == "#":
                return None
            node = TreeNode(int(val),
                            left=deserialize_helper(queue),
                            right=deserialize_helper(queue)
                            )
            return node

        queue = deque(data.split(","))
        return deserialize_helper(queue)


class TestFunctions(unittest.TestCase):
    def test_run_1(self):
        # test case
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3, left=TreeNode(4), right=TreeNode(5))
                        )
        ser = Codec()
        ans = ser.serialize(root)
        expect = '1,2,#,#,3,4,#,#,5,#,#'
        self.assertEqual(
            str(ans),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
