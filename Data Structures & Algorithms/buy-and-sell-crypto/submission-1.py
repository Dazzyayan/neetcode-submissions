class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        highest = 0

        while r < len(prices):
            p = prices[r] - prices[l]
            if p <= 0:
                l = r
            else:
                highest = p if p > highest else highest
            r += 1
        
        return highest