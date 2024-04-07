# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# осознал смысл задачи за 43 секунды
# придумал первый вариант решения за 30 секунд
# фактически это развитие идеи с двумя отсортированными списками, но теперь здесь действительно нужен итератор, так как списки находятся в массиве
# первое решение за 8 минут, ошибка - бесконечный цикл
# через 3 минуты нашел причину ошибки - я работаю с элементами списка и проверяю условия, но сам списко не меняется и поэтому условия не срабатывают
# сделал еще один список и добавлял туда односвязные списки, по которым перемещался
# 13 минут: снова ошибка lists = [[1,4,5],[1,3,4],[2,6]], Output [1,4,5]
# через минуту нашел ошибку, дело в том, что я находил локальный минимум и сразу добавлял элемент в список, тогда как минимум я мог найти только пройдясь по всем элементам списка
# 16 минут - новое решение, решил отслеживать попизицию списка с минимальным первым элементом
# пока ошибка IndexError: list index out of range: elem = lists[pos]
# спустя 20 минут я так и не нашел ошибки и пошел смотреть Solutions
# прочитав несколько вариантов решений я так и не понял, что я сделал не так
# нашел ошибку, но к этому времени уже остановил таймер, мое решение заработало


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        cur = head
        min_ = float("inf")
        lists = [elem for elem in lists if elem]
        while lists:

            for i, elem in enumerate(lists):
                if elem.val < min_:
                    min_ = elem.val
                    pos = i

            elem = lists[pos]
            cur.next = elem
            elem = elem.next
            lists[pos] = elem
            cur = cur.next
            min_ = float("inf")
            lists = [elem for elem in lists if elem]

        return head.next



#мое решение оказалось довольно медленным и я решил его оптимизировать (или поискать что-то более оптимальное среди готовых)
#мне понравилась идея сведения задачи с K листами к задаче с 2-мя листами, оно оказалось существенно более эффективным
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        cur = head

        def merge2Lists(list1, list2):
            head = ListNode()
            cur = head

            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

            cur.next = list1 if list1 else list2
            return head.next

        if lists == []:
            return head.next

        while len(lists) > 1:
            res = merge2Lists(lists[0], lists[1])
            lists = lists[2:]
            lists.append(res)

        return lists[0]