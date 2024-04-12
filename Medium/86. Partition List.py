# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        leftList = ListNode()
        rightList = ListNode()
        leftHead = leftList
        rightHead = rightList

        while head:
            if head.val < x:
                leftList.next = ListNode(head.val)
                leftList = leftList.next
            else:
                rightList.next = ListNode(head.val)
                rightList = rightList.next
            head = head.next

        leftList.next = rightHead.next

        return leftHead.next


