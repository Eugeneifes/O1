import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.data = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            del self.data[key]
        elif len(self.data) >= self.capacity:
            self.data.popitem(last=False)

        self.data[key] = value
