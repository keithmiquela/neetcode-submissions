# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverseList(head):
            prev = None
            curr = head
            temp = None
            while curr!=None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        def mergeLists(list1, list2):
            curr = list1
            alt = list2
            temp = None
            while alt != None:
                temp = curr.next
                curr.next = alt
                alt = temp
                curr = curr.next 

        length = 0
        ptr = head
        while ptr!=None:
            ptr = ptr.next
            length+=1
        
        # find half point
        length = length/2 if length%2==0 else length//2+1
        counter = 1
        ptr = head
        while counter < length:
            ptr = ptr.next
            counter+=1

        head2 = reverseList(ptr.next)
        ptr.next = None
        mergeLists(head, head2)

        