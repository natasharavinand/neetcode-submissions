class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in nums:
            if num - 1 in numSet:
                continue

            currNum = num
            while (currNum + 1) in numSet:
                currNum += 1
            
            result = max(result, currNum - num + 1)
        
        return result
        