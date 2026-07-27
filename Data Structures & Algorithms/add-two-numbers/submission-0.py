# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        carry = 0

        i = l1
        j = l2

        while i!=None or j!=None or carry!=None:
            value = carry
            if i:
                value+=i.val
                i = i.next
            if j:
                value+=j.val
                j = j.next
            ptr.val = value%10
            carry = value//10
            if not i and not j and not carry:
                break
            ptr.next = ListNode()
            ptr = ptr.next
        
        return head

