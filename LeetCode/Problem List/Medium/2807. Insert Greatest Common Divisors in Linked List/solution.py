from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        next_node = head.next

        while next_node is not None:
            divisior = min(current.val, next_node.val)
            for _ in range(divisior):
                if current.val % divisior == 0 and next_node.val % divisior == 0:
                    break
                else:
                    divisior -= 1
            divisior_node = ListNode(val=divisior, next=next_node)
            current.next = divisior_node
            current = next_node
            next_node = next_node.next
        return head
