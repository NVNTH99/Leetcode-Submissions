# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = None
        heada = None
        b = None
        headb = None
        c = head
        while c != None:
            if c.val < x:
                if heada == None:
                    heada = c
                    a = c
                else:
                    a.next = c
                    a = a.next
            else:
                if headb == None:
                    headb = c
                    b = c
                else:
                    b.next = c
                    b = b.next
            c = c.next
        if b != None:
            b.next = None
        if a != None:
            a.next = headb
        if heada != None:
            return heada
        return headb