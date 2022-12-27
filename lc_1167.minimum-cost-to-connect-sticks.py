# from typing import List
# from heapq import heappush, heapq, heapify

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        h = sticks[:]
        heapify(h)
        while len(h) > 1:
            new_item = heappop(h) + heappop(h)
            heappush(h, new_item)
            ans += new_item 
        return ans
