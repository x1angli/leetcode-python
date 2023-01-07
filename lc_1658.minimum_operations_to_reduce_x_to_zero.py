# ---
# title: 1658. Minimum Operations to Reduce X to Zero
# keywords: sliding window, double pointers 
# ---


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        arr_sum = 0
        arr_head = 0
        n = len(nums)
        ans = n+1
        for arr_tail in range(0, n):
            arr_sum += nums[arr_tail]
            while arr_sum > target and arr_head <= arr_tail:
                arr_sum -= nums[arr_head]
                arr_head += 1

            if arr_sum == target:
                ans = min(ans, n-1 + arr_head - arr_tail)

        return ans if ans <= n else -1
