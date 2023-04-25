# Definition for singly-linked list.
from typing import Optional


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None

        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        curr, prev = slow.next, None
        slow.next = None  # set the next of the slow to None to break the link
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev

        # Step 3: Merge the first half and
        # the reversed second half of the linked list
        first_half = head
        while first_half and second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2

        return None
