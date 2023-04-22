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
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ans = ListNode()
        memo = 0
        while l1 or l2 or memo:
            value = memo
            if l1:
                value += l1.val
                l1 = l1.next

            if l2:
                value += l2.val
                l2 = l2.next

            memo, value = divmod(value, 10)
            curr.next = ListNode(value)
            curr = curr.next

        return ans.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        list1 = ListNode(2, ListNode(4, ListNode(3, None)))
        list2 = ListNode(5, ListNode(6, ListNode(4, None)))
        expect = ListNode(7, ListNode(0, ListNode(8, None)))
        self.assertEqual(sum_link_list(self.solution.addTwoNumbers(list1,
                                                                   list2)
                                       ),
                         sum_link_list(expect),
                         "incorrect, expect is " + str(sum_link_list(
                             expect)
        )
        )

    def test_run_2(self):
        # test case
        list1 = ListNode(0, None)
        list2 = ListNode(0, None)
        expect = ListNode(0, None)
        self.assertEqual(sum_link_list(self.solution.addTwoNumbers(
            list1,
            list2)
        ),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(
                expect
            )
        )
        )

    def test_run_3(self):
        # test case
        list1 = ListNode(9, ListNode(9, ListNode(9, ListNode(
            9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        list2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        expect = ListNode(8, ListNode(9, ListNode(9, ListNode(
            9, ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))))))
        self.assertEqual(sum_link_list(self.solution.addTwoNumbers(
            list1,
            list2
        )),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
