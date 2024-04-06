# осознал смысл за минуту

# через 8 минут после начала придумал идею решения
# 5 указателей: head, one_before, potential, one_after, end
# между potential и end у нас расстояние n, пытаемся нащупать end, после того как нащупали перекидываем мостик от one_before до one_after через potential

# первое решение через 15минут
# ошибка AttributeError: 'NoneType' object has no attribute 'next'
# head = [1,2,3,4,5], n=2
# забыл увеличить счетчик dist, ошибку нашел только через 6 мин

# ошибка (на том же примере) head = [1,2,3,4,5], n=2, Expected [1,2,3,5], Output [1,2,4,5]
# ошибка AttributeError: 'NoneType' object has no attribute 'next'
# head = [1,2,3], n =3
# очень много корнер кейсов, решить не успел, идем в спокойном режиме

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None
        if not head.next.next and n == 1:
            head.next = None
            return head
        if not head.next.next and n == 2:
            head = head.next
            return head

        one_before = head
        potential, one_before_end = head.next, head.next
        one_after, end = head.next.next, head.next.next

        if n == 1:
            while end.next:
                one_before_end = one_before_end.next
            one_before_end.next = None
            return head

        if n == 2:
            while end.next:
                one_before = one_before.next
                potential = potential.next
                end = end.next
            one_before.next = end
            return head

        dist_ = 1
        while dist_ < n:
            end = end.next
            dist_ += 1

        while end.next:
            one_before = one_before.next
            potential = potential.next
            one_after = one_after.next
            end = end.next

        one_before.next = one_after

        return head


#до чего додумался сам
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        if not head.next.next:
            if n == 1:
                head.next = None
                return head
            if n == 2:
                head = head.next
                return head

        if not head.next.next.next:
            if n == 1:
                head.next.next = None
                return head
            if n == 2:
                head.next = head.next.next
                return head
            if n == 3:
                head = head.next
                return head

        if n == 1:
            point1 = head
            point2 = head.next
            while point2.next:
                point2 = point2.next
                point1 = point1.next
            point1.next = None
            return head

        if n == 2:
            point1 = head
            point2 = head.next
            point3 = head.next.next
            while point3.next:
                point3 = point3.next
                point2 = point2.next
                point1 = point1.next
            point1.next = point2.next
            return head

        prev = head
        to_remove = head.next
        end = head.next.next

        dist = 1
        while dist < n:
            end = end.next
            dist += 1

        if end.next == None:
            head = head.next
            return head

        while end.next:
            to_remove = to_remove.next
            end = end.next
            prev = prev.next
        prev.next.next = to_remove.next.next
        return head


#самое близкое из того, что подсмотрел и сам понял
"""
Здесь применяется стандартный прием с 2-мя указателями: быстрым и медленным
Сначала быстрый указатель отходит на n шагов вперед от медленного
Это нужно для того, чтобы когда мы начали быстрым указателем нащупывать конец, медленный
указатель подтягивался за ним и в конечном итоге указал на элемент, через который нужно перепрыгнуть
Есть 1 корнер-кейс - в случае если список состоит из 1 элемента, fast.next сразу укажет на None
Это условие мы пропишем отдельно
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head