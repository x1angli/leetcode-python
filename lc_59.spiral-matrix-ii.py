class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        ans = [([0] * n ) for _ in range(n)]

        l = 0
        r = n - 1
        t = 0
        b = n - 1

        num = 1 
        total_laps = (n+1)//2
        for _ in range(total_laps):
            for i in range(l, r + 1): 
                ans[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): 
                ans[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): 
                ans[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): 
                ans[i][l] = num
                num += 1
            l += 1
        return ans
