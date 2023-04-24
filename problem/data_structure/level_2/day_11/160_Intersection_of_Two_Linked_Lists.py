# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self,
                            headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        dic = {}
        while headA:
            dic[headA] = 1
            headA = headA.next

        while headB:
            if dic.get(headB) is not None:
                return headB
            headB = headB.next

        return None
