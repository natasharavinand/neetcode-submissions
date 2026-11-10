class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1
        totalWater = 0

        while l <= r:
            if height[l] < height[r]:
                currWater = maxLeft - height[l]
                if currWater > 0:
                    totalWater += currWater
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                currWater = maxRight - height[r]
                if currWater > 0:
                    totalWater += currWater
                maxRight = max(maxRight, height[r])
                r -= 1   
        
        return totalWater
