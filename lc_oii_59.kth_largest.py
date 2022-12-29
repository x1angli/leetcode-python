# problem desc & input spec
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

from heapq import heapify, heappushpop, nlargest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nlargest(k, nums)
        heapify(self.h)
        self.k = k

    def add(self, val: int) -> int:
        h = self.h                  # shorthand
        if len(h) < self.k:
            heappush(h, val)
        elif val > h[0]:
            heappushpop(h, val)
        return h[0]


