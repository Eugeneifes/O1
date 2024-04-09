# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#очень непонятная формулировка и задача, но вроде понял (1.5 минуты на понимание)
#3 минуты, 20 секунд, вроде понял: идем парами, первому присваиваем 1.next.next, а второму первый, обрабатываем корней кейсы
#порядок условий в if важен, оказывается if not head or not head.next и if not head.next or not head это существенная разница


#решение через четный счетчик (когда значение четное - делаем swap, иначе простро двигаемся)
#двигаемся на одну ноду вперед а не на две тем самым всегда контролируя условие того, что не вывалимся за границу списка
#при этом происходит swap значений, а не указателей, что как-бы не должно работать (по идее)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1 # 1 based index, because we need to swap when we reach at element 2
        prev, curr = None, head
        while curr:
            if count % 2 == 0: # checking condition, when we reach at end of pair nodes then we swap
                prev.val, curr.val = curr.val, prev.val
            prev = curr # update prev
            curr = curr.next # move forward
            count += 1 # increse index
        return head


#не очень элегентное, но мое решение
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        first = head
        second = head.next

        while second.next and second.next.next:
            first.val, second.val = second.val, first.val
            first = second.next
            second = second.next.next
        first.val, second.val = second.val, first.val

        return head


#с обменом указателями, а не значениями (что как бы правильно и на самом деле соответсвует условию задачи, в отличие от предыдущих решений)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummyNode.next