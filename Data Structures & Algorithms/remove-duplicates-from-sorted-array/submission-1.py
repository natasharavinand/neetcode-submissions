class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        ptr = 0

        while ptr < len(nums) - 1:
            print("ptr: ", ptr, " k: ", k)
            if nums[ptr + 1] == nums[ptr]:
                ptr += 1
                print("skipping")
                continue
            nums[k] = nums[ptr]
            k += 1
            ptr += 1
        
        if nums[k] != nums[-1]:
            nums[k] = nums[-1]
        
        return k + 1

        