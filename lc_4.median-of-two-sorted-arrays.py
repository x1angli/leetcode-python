
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        # binary search, find the pseudo-median left, which will be recorded as m1
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right :
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 
        
        c1 = max(nums1[m1-1] if m1 > 0 else float('-inf'), nums2[m2-1] if m2 > 0 else float('-inf') )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float('inf'), nums2[m2] if m2 < n2 else float('inf'))
        return (c1 + c2) / 2


class MergeSortSolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        MAX_INF = 9999999999
        
        quot, rmnd = divmod (len(nums1) + len(nums2), 2)        
        if rmnd == 0:   # even number
            med_idxs = (quot-1, quot)
        else:           # odd number
            med_idxs = (quot, )
            
        iter_1 = iter(nums1)
        iter_2 = iter(nums2)
        val_1 = next(iter_1, MAX_INF)
        val_2 = next(iter_2, MAX_INF)
        
        i = 0
        med_sum = []
        while i <= med_idxs[-1]:
            if val_1 > val_2:
                if i in med_idxs:
                    med_sum.append(val_2)
                val_2 = next(iter_2, MAX_INF)
            else:
                if i in med_idxs:
                    med_sum.append(val_1)
                val_1 = next(iter_1, MAX_INF)
            i += 1
        
        return mean(med_sum)
