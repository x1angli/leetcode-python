# Dynamic programming solution
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        long_pos = -prices[0]   # the max profit assuming we are holding the given stock, but haven't sold it yet
        covered_pos = 0         # the max profit assuming we are not holding the given stock
        
        for i in range(1, len(prices)):
            price_i = prices[i]
            long_pos, covered_pos = max(long_pos, covered_pos-price_i) , max(covered_pos, long_pos+price_i-fee)
        
        return covered_pos

# Very smart, but counter intuitive solution
class SolutionGreedyAlgo:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = 0
        buy_price = None
        
        for i in range(len(prices)):
            price_i = prices[i]
            if buy_price is None:
                buy_price = price_i 
            elif price_i > buy_price + fee:
                ans += price_i - fee - buy_price    # punchline
                buy_price = price_i-fee             # punchline
            elif price_i < buy_price:
                buy_price = price_i
                
        return ans
