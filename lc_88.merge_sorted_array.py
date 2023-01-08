class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1_ri, n2_ri = m-1, n-1

        for n1_wi in range (m+n-1, -1, -1):
            if n2_ri < 0:
                break
            
            if n1_ri < 0 or (nums1[n1_ri] < nums2[n2_ri]):
                nums1[n1_wi] = nums2[n2_ri]
                n2_ri -= 1
                continue
            
            if nums1[n1_ri] >= nums2[n2_ri]:
                nums1[n1_wi] = nums1[n1_ri]
                n1_ri -= 1
                continue
