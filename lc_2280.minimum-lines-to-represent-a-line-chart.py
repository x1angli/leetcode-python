# Note: this challenge is intendede to be tricky, traditional dy/dx won't work! 

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n == 1:
            return 0
        if n == 2:
            return 1
            
        stockPrices.sort()
        ans = 1
        dy1 = stockPrices[1][1] - stockPrices[0][1]
        dx1 = stockPrices[1][0] - stockPrices[0][0]
        
        for i in range(2, n):
            dy = stockPrices[i][1] - stockPrices[i-1][1]
            dx = stockPrices[i][0] - stockPrices[i-1][0]
            
            if (dy * dx1 != dx* dy1):       
                ans += 1 
            
            dy1 = dy
            dx1 = dx

        return ans
