class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        ptr = 0

        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[ptr] = nums[i]
            ptr += 1
        
        return len(seen)
        