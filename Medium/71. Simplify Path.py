"""
Алгоритм подразумевает разбивание строки по разделителю "/" с последующим созданием очереди
"""
class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for elem in path.split("/"):
            if elem == "..":
                stack = stack[:-1]
            elif elem == "." or not elem:
                pass
            else:
                stack.append(elem)

        return "/" + "/".join(stack)