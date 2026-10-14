# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        if result == result[::-1]:
            return True
        return False