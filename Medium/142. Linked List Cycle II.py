# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()

        if not head:
            return None

        while head.next:
            if head not in hashSet:
                hashSet.add(head)
            else:
                return head
            head = head.next
        return None
