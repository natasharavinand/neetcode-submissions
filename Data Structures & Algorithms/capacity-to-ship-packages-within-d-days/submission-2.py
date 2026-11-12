import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysNeeded(capacity):
            daysCount = 1
            currCapacity = capacity

            for weight in weights:
                if currCapacity - weight < 0:
                    daysCount += 1
                    currCapacity = capacity
                currCapacity -= weight

            return daysCount
            
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            # If this weight allows us to ship with days, check for a lower weight
            if daysNeeded(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


        