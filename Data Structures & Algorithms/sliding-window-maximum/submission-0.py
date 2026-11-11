class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        l = 0
        windowMax = float("-infinity")
        window = {}

        for r in range(len(nums)):
            window[nums[r]] = window.get(nums[r], 0) + 1

            if r - l + 1 == k:
                result.append(max(window.keys()))

                window[nums[l]] -= 1 

                if window[nums[l]] == 0:
                    del window[nums[l]]

                l += 1
    

        return result
        