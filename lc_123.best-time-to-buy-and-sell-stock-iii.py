class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0

        for price_i in prices[1:]:
            buy1  = max(buy1,  -price_i)
            sell1 = max(sell1, buy1 + price_i)
            buy2  = max(buy2,  sell1 - price_i)
            sell2 = max(sell2, buy2 + price_i)
            
        return sell2
      
