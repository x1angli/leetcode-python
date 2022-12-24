class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 2             # 1 and n
        i = 2
        while i * i < n:
            if n % i == 0:
                cnt += 2    # i and n/i
            i += 1
        
        if i * i == n:
            cnt += 1
            
        return cnt == 3
