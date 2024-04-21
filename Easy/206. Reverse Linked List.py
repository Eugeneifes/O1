# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#самый часто используемый метод
#нам нужно, чтобы текущий узел указывал на предыдущий, но для этого нам нужно хранить указатель на предыдущий


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        # O(n) time | O(1) space
        if not head or not head.next:
            return head

        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


#более элегантное решение на рекурсию
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return p
