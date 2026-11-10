class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1
        totalWater = 0

        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                totalWater += max(0, maxLeft - height[l])
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                totalWater += max(0, maxRight - height[r])
                r -= 1
        
        return totalWater
