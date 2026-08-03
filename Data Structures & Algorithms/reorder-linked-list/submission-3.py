# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        
        def findHalf(head) -> int:
            length = 0
            temp = head
            while temp != None:
                temp = temp.next
                length += 1

            half = math.ceil(length / 2)
            return half

        def findRight(head, half) -> ListNode:
            counter = 0
            temp = head
            prev = None
            while counter < half:
                prev = temp
                temp = temp.next
                counter += 1
            if prev:
                prev.next = None
            return temp
        
        def reverseList(head) -> ListNode:
            if not head:
                return head
            prev = None
            curr = head
            nextNode = head.next
            while curr != None:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            return prev
        
        def mergeLists(head1, head2) -> ListNode:
            i = head1
            j = head2
            main_head = i

            while i != None:
                temp = i.next
                i.next = j
                i = j
                j = temp
            
            return main_head
        half = findHalf(head)
        right = findRight(head, half)
        right = reverseList(right)
        head = mergeLists(head, right)

            

        
        

                