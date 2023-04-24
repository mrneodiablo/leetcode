# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_link_list(linkList: ListNode):
    a = 0
    while linkList is not None:
        a += int(linkList.val)
        linkList = linkList.next
    return a


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        for i in range(0, len(lst)-1, 2):
            lst[i], lst[i+1] = lst[i+1], lst[i]

        ans = ListNode(0)
        temp = ans
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return ans.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expect = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))

        self.assertEqual(sum_link_list(self.solution.swapPairs(head)),
                         sum_link_list(expect),
                         "incorrect, expect is " + str(sum_link_list(expect))
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
