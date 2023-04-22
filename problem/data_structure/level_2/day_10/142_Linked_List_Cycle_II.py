from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        while head:
            if head in dic:
                break

            dic[head] = 1
            head = head.next
        return head
