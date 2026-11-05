class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numbers = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in previous_numbers:
                return [previous_numbers[complement], index]
            previous_numbers[num] = index
        
        return -1
        