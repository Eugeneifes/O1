class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque = [value] + self.deque
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.deque) > 0:
            front = self.deque[0]
            return front
        return -1

    def getRear(self) -> int:
        if len(self.deque) > 0:
            rear = self.deque[-1]
            return rear
        return -1

    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
