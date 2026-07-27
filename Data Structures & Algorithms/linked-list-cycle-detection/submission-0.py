# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        i=head
        j=head.next
        while j != None:
            if i.val == j.val:
                return True
            i=i.next
            if not j.next:
                return False
            j=j.next.next
        return False