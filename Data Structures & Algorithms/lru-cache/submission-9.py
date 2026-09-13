class LRUCache:

    def __init__(self, capacity: int):
        self.cache_list = [] # storing the key and value in the list
        self.cap = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache_list)):
            if self.cache_list[i][0] == key:
                tmp = self.cache_list.pop(i)
                self.cache_list.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache_list)):
            if self.cache_list[i][0] == key:
                tmp = self.cache_list.pop(i)
                self.cache_list.append([key, value])
                return
        if len(self.cache_list) == self.cap:
            self.cache_list.pop(0)
        self.cache_list.append([key, value])