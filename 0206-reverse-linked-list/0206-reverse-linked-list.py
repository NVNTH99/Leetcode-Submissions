# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(a,b):
            if b == None:
                return a
            c = b.next
            b.next = a
            return reverse(b,c)
        
        return reverse(None,head)