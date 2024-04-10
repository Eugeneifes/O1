# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


""""
k=2
[1, ] -> [2, ] -> [3, ]    ||    -> [4, ] -> [5, ] -> None


step1: [5, ] -> [1, ]
step2: head -> [4, ]
step3: [3, ] -> None


head -> [4, ] -> [5, ] -> [1, ] -> [2, ] -> [3, ] -> None

"""


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        curr, size = head, 1
        while curr.next:
            curr = curr.next
            size += 1

        k = k % size
        k = size - k
        curr.next = head
        while k:
            curr = curr.next
            k -= 1

        head = curr.next
        curr.next = None

        return head
