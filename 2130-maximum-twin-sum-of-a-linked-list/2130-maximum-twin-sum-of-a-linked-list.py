# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = 0
        x = head
        while x!=None:
            l += 1
            x = x.next
        sumlist = list()
        x = head
        for i in range(l//2):
            sumlist.append(x.val)
            x = x.next
        l = l//2 -1
        while l>=0:
            sumlist[l] += x.val
            x = x.next
            l -= 1
        return max(sumlist)