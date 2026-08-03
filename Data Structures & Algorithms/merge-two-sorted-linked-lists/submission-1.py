# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        i = list1
        j = list2
        
        if j == None:
            return i
        if i == None:
            return j

        if i.val <= j.val:
            head = i
            i = i.next
        else:
            head = j
            j = j.next

        curr = head
        
        while i != None and j != None:
            if i.val <= j.val:
                curr.next = i
                i = i.next
            else:
                curr.next = j
                j = j.next
            
            curr = curr.next
        
        if j:
            curr.next = j
        if i:
            curr.next = i

        return head

