# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mapping = {}
        while head:
            if head not in mapping.keys():
                mapping[head] = 1
            else:
                return True
            head = head.next
        return False
