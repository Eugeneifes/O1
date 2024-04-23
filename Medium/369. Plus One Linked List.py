# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def reverse(l):
            prev = None
            curr = l
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        reverse_head = reverse(head)
        dummy = res = ListNode(0)
        carry = 1

        while reverse_head or carry:
            if reverse_head:
                carry += reverse_head.val
                reverse_head = reverse_head.next
            res.next = ListNode(carry % 10)
            res = res.next
            carry = carry // 10

        res = reverse(dummy.next)

        return res
