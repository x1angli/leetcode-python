class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        res = 0 
        while i < n:
            for _ in range(3):
                if i >= n: 
                    break
                if s[i] == 'X':
                    res += 1
                    i += 3
                    break
                i += 1 
        return res
