# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self,
                      head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst2 = []
        for i in range(0, len(lst), k):
            b = lst[i:k+i]
            if len(b) == k:
                b = b[::-1]
            lst2 += b
        a = ListNode(0)
        temp = a
        for i in lst2:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
