from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_link_list(linkList: ListNode):
    a = 0
    while linkList.next is not None:
        a += int(linkList.val)
        linkList = linkList.next
    return a


class Solution:
    def removeElements(self,
                       head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        current_node = dummy
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        val = 6
        head = ListNode(1,
                        ListNode(2,
                                 ListNode(6,
                                          ListNode(3,
                                                   ListNode(4,
                                                            ListNode(5,
                                                                     ListNode(
                                                                         6,
                                                                         None)
                                                                     )
                                                            )
                                                   )
                                          )
                                 )
                        )

        expect = ListNode(1, ListNode(2, ListNode(
            3, ListNode(4, ListNode(5, None)))))
        self.assertEqual(
            sum_link_list(self.solution.removeElements(head, val)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
