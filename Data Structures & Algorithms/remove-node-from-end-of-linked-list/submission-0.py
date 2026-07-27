# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findLength():
            ptr = head
            length = 0
            while ptr!=None:
                ptr = ptr.next
                length+=1
            return length
        
        length = findLength()

        # 0-indexed
        index = length - n
        if index == 0:
            return head.next
        
        prev = None
        curr = head
        counter = 0
        while counter<index:
            prev = curr
            curr = curr.next
            counter+=1

        prev.next = curr.next
        curr = None

        return head
