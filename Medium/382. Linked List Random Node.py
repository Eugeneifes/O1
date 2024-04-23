# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:

        reservoir = self.head.val

        i = 2
        next_ = self.head.next
        while next_:
            if random.random() < 1 / i:
                reservoir = next_.val
            i += 1
            next_ = next_.next
        return reservoir

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()