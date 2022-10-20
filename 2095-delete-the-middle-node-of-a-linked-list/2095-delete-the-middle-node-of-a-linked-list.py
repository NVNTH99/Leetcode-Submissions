# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = head
        z = None
        while x and x.next:
            z = y
            y = y.next
            x = x.next.next
        if z!=None:
            z.next = y.next
        else:
            head = None
        return head