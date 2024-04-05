# придумал решение за 1,5 минуты
# прохожусь по обоим массивам слева направо, складываю элементы, если > 10, прибавляю остаток от деления на 10 к следующему разряду

# первое решение через 10 минут
# щикба TypeError: object of type 'ListNode' has no len()
# это не List, для задания было указано, что структура данных своя, надо быть внимательнее

from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = []
        add_ = 0
        if len(l1) > len(l2):
            for elem in range(len(l1) - len(l2)):
                l2.append(0)
        elif len(l2) > len(l1):
            for elem in range(len(l2) - len(l1)):
                l1.append(0)

        for i in range(len(l1)):

            result.append((l1[i] + l2[i]) / 10 + add_)
            if l1[i] + l2[i] >= 10:
                add_ = (l1[i] + l2[i]) // 10
            else:
                add_ = 0

        if add_ != 0:
            result.append(add_)

        return result


# второе решение через 15 минут
# ошибка l1 =[2,4,3], l2 =[5,6,4], expected [7,0,8], output []
# я ничего не возвращаю в result, сразу поправил return и отправил 3 решение
# ошибка l1 =[2,4,3], l2 =[5,6,4], expected [7,0,8], output [0]
# итерируюсь по списку и не храню указатель на начало

# третье решение через 10 минут, проанализировал решил добавить head
# ошибка l1 =[2,4,3], l2 =[5,6,4], expected [7,0,8], output [7, 10, 0]
# мне надо брать остаток от деления на 10 всех слагаемых, а не только val списков


# четвертое решение Time Limit Exceeded (причину сначала не понял, потом увидел, что я не меняю указатель и цикл становится бесконечным)
# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        add_ = 0
        result_ListNode = ListNode()
        head = result_ListNode

        while l1.next and l2.next:
            result_ListNode.val = (l1.val + l2.val + add_) / 10
            result_ListNode.next = ListNode()

            if l1.val + l2.val + add_ >= 10:
                add_ = (l1.val + l2.val + add_) // 10
            else:
                add_ = 0

            l1 = l1.next
            l2 = l2.next
            result_ListNode = result_ListNode.next

        while l1.next or l2.next:
            if l1.next:
                result_ListNode.val = (l1.val + add_) / 10
                result_ListNode.next = ListNode()

                if l1.val + add_ >= 10:
                    add_ = (l1.val + add_) // 10
                else:
                    add_ = 0

            else:
                result_ListNode.val = (l2.val + add_) / 10
                result_ListNode.next = ListNode()

                if l2.val + add_ >= 10:
                    add_ = (l2.val + add_) // 10
                else:
                    add_ = 0

        result_ListNode.next = None

        return head


#итого не успел, разбираюсь самостоятельно без таймера

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        add_ = 0
        result_ListNode = ListNode()
        head = result_ListNode

        while l1.next and l2.next:

            if l1.val + l2.val + add_ >= 10:
                result_ListNode.val = (l1.val + l2.val + add_) % 10
                add_ = (l1.val + l2.val + add_) // 10
            else:
                result_ListNode.val = (l1.val + l2.val + add_)
                add_ = 0
            result_ListNode.next = ListNode()

            l1 = l1.next
            l2 = l2.next
            result_ListNode = result_ListNode.next

        # case:
        # 2->4->3->None
        # 5->6->4->None
        if l1.next is None and l2.next is None:
            if l1.val + l2.val + add_ >= 10:
                result_ListNode.val = (l1.val + l2.val + add_) % 10
                add_ = (l1.val + l2.val + add_) // 10
                result_ListNode.next = ListNode()

                result_ListNode = result_ListNode.next

                result_ListNode.val = add_
                result_ListNode.next = None
                return head
            else:
                result_ListNode.val = l1.val + l2.val + add_
                result_ListNode.next = None
                return head


        # case:
        # 2->4->3->None
        # 5->6->4->7->10->20->None
        elif l2.next is not None and l1.next is None:

            if l1.val + l2.val + add_ >= 10:
                result_ListNode.val = (l1.val + l2.val + add_) % 10
                add_ = (l1.val + l2.val + add_) // 10
            else:
                result_ListNode.val = l1.val + l2.val + add_
                add_ = 0

            result_ListNode.next = ListNode()
            result_ListNode = result_ListNode.next
            l2 = l2.next

            while l2.next:
                if l2.val + add_ >= 10:
                    result_ListNode.val = (l2.val + add_) % 10
                    add_ = (l2.val + add_) // 10
                else:
                    result_ListNode.val = (l2.val + add_)
                    add_ = 0
                result_ListNode.next = ListNode()

                l2 = l2.next
                result_ListNode = result_ListNode.next

            if l2.val + add_ >= 10:
                result_ListNode.val = (l2.val + add_) % 10
                add_ = (l2.val + add_) // 10
                result_ListNode.next = ListNode()
                result_ListNode = result_ListNode.next

                result_ListNode.val = add_
                result_ListNode.next = None
                return head
            else:
                result_ListNode.val = l2.val + add_
                result_ListNode.next = None
                return head


        # case:
        # 5->6->4->7->10->20->None
        # 2->4->3->None
        elif l1.next is not None and l2.next is None:

            if l1.val + l2.val + add_ >= 10:
                result_ListNode.val = (l1.val + l2.val + add_) % 10
                add_ = (l1.val + l2.val + add_) // 10
            else:
                result_ListNode.val = l1.val + l2.val + add_
                add_ = 0

            result_ListNode.next = ListNode()
            result_ListNode = result_ListNode.next
            l1 = l1.next

            while l1.next:
                if l1.val + add_ >= 10:
                    result_ListNode.val = (l1.val + add_) % 10
                    add_ = (l1.val + add_) // 10
                else:
                    result_ListNode.val = (l1.val + add_)
                    add_ = 0
                result_ListNode.next = ListNode()

                l1 = l1.next
                result_ListNode = result_ListNode.next

            if l1.val + add_ >= 10:
                result_ListNode.val = (l1.val + add_) % 10
                add_ = (l1.val + add_) // 10

                result_ListNode.next = ListNode()
                result_ListNode = result_ListNode.next

                result_ListNode.next = None
                result_ListNode.val = add_

                return head
            else:
                result_ListNode.val = l1.val + add_
                result_ListNode.next = None
                return head

"""
l1 = [5,6,7,1,1]
l2 = [8,9,3]

L1 = ListNode()
head1 = L1

for elem in l1:
  L1.val = elem
  L1.next = ListNode()
  L1 = L1.next 

l_1 = []
while head1.next:
  l_1.append(head1.val)
  head1=head1.next

print("->".join([str(elem) for elem in l_1]))

L2 = ListNode()
head2 = L2

for elem in l2:
  L2.val = elem
  L2.next = ListNode()
  L2 = L2.next 

l_2 = []
while head2.next:
  l_2.append(head2.val)
  head2=head2.next

print("->".join([str(elem) for elem in l_2]))


s = Solution()
res = s.addTwoNumbers(l1=head1, l2 = head2)

res_ = []
while res.next:
  res_.append(res.val)
  res=res.next

print("->".join([str(elem) for elem in res_]))
"""

