# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        i = head.next
        j = head.next.next

        while i!=j and i and j:
            i = i.next
            
            if not j.next:
                return False

            j = j.next.next

        if not i or not j:
            return False
        else:
            return True