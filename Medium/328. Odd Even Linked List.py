# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        odd = ListNode()
        odd_head = odd
        even = ListNode()
        even_head = even

        idx = 1
        while curr:
            if idx % 2 == 0:
                even.next = ListNode(curr.val)
                even = even.next
            else:
                odd.next = ListNode(curr.val)
                odd = odd.next

            idx += 1
            curr = curr.next

        odd_head = odd_head.next
        even_head = even_head.next
        odd.next = even_head
        even.next = None
        return odd_head
