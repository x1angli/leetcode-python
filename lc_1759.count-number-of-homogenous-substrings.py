from itertools import groupby   

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0 
        for key, group in groupby(s):
            group_len = len(list(group))
            res += group_len * (group_len + 1) // 2
        return res % (10**9+7)
