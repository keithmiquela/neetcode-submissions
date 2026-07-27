# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        head = list1 if list1.val < list2.val else list2
        alt = list2 if list1.val < list2.val else list1

        curr = head
        temp = curr.next

        while curr:
            if not temp:
                curr.next = alt
                break
            if temp.val <= alt.val:
                curr = temp
                temp = curr.next
                continue
            curr.next = alt
            alt = temp
            curr = curr.next
            temp = curr.next

        return head

