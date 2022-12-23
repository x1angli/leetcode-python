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
