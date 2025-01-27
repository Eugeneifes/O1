#мое решение
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c == 0:
            return True

        a=0
        b=1

        while a<=b:
            if a*a+b*b == c:
                return True
            elif a*a+b*b > c:
                b-=1
                a+=1
            elif a*a+b*b < c:
                b+=1
        return False
