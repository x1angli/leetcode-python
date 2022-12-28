class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = defaultdict(int)
        for i, nums in enumerate((nums1, nums2, nums3)):
            for x in nums:
                mask[x] |= 1 << i
        return [x for x, m in mask.items() if m & (m - 1)]


class SetOperationSolution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set2_3 = (set(nums1) & set(nums2)) | (set(nums1) & set(nums3)) | (set(nums2) & set(nums3))
        return list(set2_3)
