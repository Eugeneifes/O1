# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head -> [3, ] -> [5, ] -> None
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummyNode = ListNode()
        dummyNode.next = head

        prev = dummyNode

        while left > 1:
            head = head.next
            prev = prev.next
            left -= 1
            right -= 1

        tail1 = prev
        tail2 = head

        while right:
            third = head.next
            head.next = prev
            prev = head
            head = third
            right -= 1

        if tail1:
            tail1.next = prev
        else:
            head = prev
        tail2.next = head
        return dummyNode.next