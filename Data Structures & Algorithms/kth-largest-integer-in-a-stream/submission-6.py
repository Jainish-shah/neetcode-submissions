class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.arr = k, nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]

