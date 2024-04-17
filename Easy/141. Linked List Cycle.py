# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#более простое решения, но зато сам к нему пришел
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashSet = set()
        if not head:
            return False

        while head.next:
            if head in hashSet:
                return True
            hashSet.add(head)
            head = head.next
        return False