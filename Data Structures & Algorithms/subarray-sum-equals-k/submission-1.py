class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}

        prefix = 0
        result = 0

        for i in range(len(nums)):
            prefix += nums[i]
            complement = prefix - k
            result += prefix_sums.get(complement, 0)
            prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1
        
        return result

