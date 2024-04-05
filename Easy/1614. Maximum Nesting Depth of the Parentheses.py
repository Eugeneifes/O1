# вложенные скобки
# определить элемент, который находится на наибольшей глубине в скобках и вернуть саму глубину


# за 3 минуты понял что делать
# проходимся по массиву (строке) слева направо, считаем скобки: если скобка прямая (открывающая) - прибавляем, если обратная (закрывающая) - вычитаем, в конце выводим max

# за 2 минуты реализовал первое решение: ошибка
# UnboundLocalError: cannot access local variable 'max'
# Стоит обращать внимание на нейминг переменных, чтобы не запутаться

# второй запуск - ошибка, s = "(1+(2*3)+((8)/4))+1", output: 1 expected: 3 (уменьшил не счетчик скобок, а переменную max_, которая отвечает за глубину)

# третий запуск - успешно, задача решена за 6 минут

class SolutionMy:
    def maxDepth_my(self, s: str) -> int:
        count = 0
        max_ = 0
        for elem in s:
            if elem == "(":
                count += 1
                max_ = max(count, max_)

            elif elem == ")":
                count -= 1

        return max_


# 2 минуты подумал над оптимизацией решения, ничего не придумал, пошел смотреть Solutions

class SolutionOpt:
    def maxDepth_opt(self, s):
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                if max_num < count:
                    max_num = count
            if i == ")":
                count -= 1
        return(max_num)

# итог - самое оптимальное решение по сути такое же, как у меня, у меня оно более элегантное (компактное)
# результат в зеленой зоне
# Runtime 34 ms, Beats 66.39% of users with Python3
# Memory 16.48 MB, Beats 90.60% of users with Python3