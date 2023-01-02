from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        idx_n1 = {n:idx for idx,n in enumerate(nums1)}
        ranks = [idx_n1[n] for n in nums2]
        ans = 0
        sl = SortedList()
        sl.add(ranks[0])
        for i in range(1, n-1):     # Could also be (0, n) with minor tweak
            y = ranks[i]            
            left_cnt = sl.bisect_left(y)       # total count of x's that is smaller than y
            right_cnt = (n - 1 - y) - (i - left_cnt)
            ans += left_cnt * right_cnt
            sl.add(y)
        return ans
    
class InefficientSolution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:  
        idx_n2 = {n:idx for idx,n in enumerate(nums2)}
        ranks = [idx_n2[num] for num in nums1]
        
        ans = 0 
        n = len(rank)
        for i in range(n-2):
            for j in range(i+1, n-1):
                if ranks [j] < ranks[i]:
                    continue
                for k in range(j+1, n):
                    if ranks[k] < ranks[j] or ranks[k] < ranks[i]:
                        continue
                    ans += 1
        return ans
