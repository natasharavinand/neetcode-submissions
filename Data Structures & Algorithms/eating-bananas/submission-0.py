import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingRate = max(piles)
        
        left = 1
        right = maxEatingRate

        while left <= right:
            k = (left + right) // 2

            totalHoursNeeded = 0

            for pile in piles:
                totalHoursNeeded += math.ceil(pile / k)

            if totalHoursNeeded <= h:
                right = k - 1
            else:
                left = k + 1
        
        return left

            

        