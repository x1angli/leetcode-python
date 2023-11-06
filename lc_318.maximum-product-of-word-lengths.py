class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ord_a = ord('a')
        maskLenMap = defaultdict(int)
        for word in words:
            mask = 0
            for c in list(word):
                mask |= 1 << ord(c)-ord_a
            maskLenMap[mask] = max(len(word), maskLenMap[mask])
        
        ans = 0
        for mask1, mask2 in combinations(maskLenMap, 2):
            if not mask1 & mask2:
                ans = max(ans, maskLenMap[mask1] * maskLenMap[mask2])
        
        return ans
    
