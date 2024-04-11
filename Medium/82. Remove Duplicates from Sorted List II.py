# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
head -> [1, ] -> [1, ] -> [1, ] -> [2, ] -> [3, ] -> None
"""


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        dummyNode.next = head
        pred = dummyNode

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next

        return dummyNode.next

#очень элегантное решение через условное движение и последующую проверку того, что движение имело место быть
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode
        curr = head

        while curr:

            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next

        return dummyNode.next




