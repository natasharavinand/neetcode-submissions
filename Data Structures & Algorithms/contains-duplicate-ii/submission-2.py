class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        window_start = 0

        for window_end in range(len(nums)):
            if len(window) > k:
                window.remove(nums[window_start])
                window_start += 1
            
            if nums[window_end] in window:
                return True
            
            window.add(nums[window_end])
        
        return False