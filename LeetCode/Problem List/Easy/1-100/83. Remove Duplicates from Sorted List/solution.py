# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            next_node = current.next
            if next_node.val == current.val:
                current.next = next_node.next
            else:
                current = current.next
        return head
