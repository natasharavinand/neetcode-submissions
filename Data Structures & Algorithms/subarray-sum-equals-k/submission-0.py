class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        prefix = 0
        result = 0

        for i in range(len(nums)):
            prefix += nums[i]
            complement = prefix - k
            if complement in prefix_sums:
                result += prefix_sums[complement]

            prefix_sums[prefix] += 1
        
        return result

