# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/remove-linked-list-elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                if prev:
                    prev.next = temp.next
                else:
                    head = temp.next
            else:
                prev = temp
            temp = temp.next    
        return head