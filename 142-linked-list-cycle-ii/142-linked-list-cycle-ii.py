# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        while b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                break
        if b is not None and b.next is not None:
            a = head
            while a != b:
                a = a.next
                b = b.next
            return a
        else:
            return None
        