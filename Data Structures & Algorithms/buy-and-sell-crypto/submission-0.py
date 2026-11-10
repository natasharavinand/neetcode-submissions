class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        maxProfit = 0

        for window_end in range(len(prices)):
            maxProfit = max(maxProfit, prices[window_end] - prices[window_start])
            if prices[window_end] < prices[window_start]:
                window_start = window_end
        
        return maxProfit


        