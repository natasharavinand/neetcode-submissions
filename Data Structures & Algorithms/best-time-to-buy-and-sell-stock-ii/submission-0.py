class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        profit = 0
        ownedPrice = -1

        for price in prices:
            if (price <= ownedPrice) or ownedPrice == -1:
                ownedPrice = price
            else:
                profit += price - ownedPrice
                ownedPrice = price
        
        return profit

        