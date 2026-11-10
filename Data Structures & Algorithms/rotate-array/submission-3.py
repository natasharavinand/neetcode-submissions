class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _rotate(nums, left, right):
            l = left
            r = right

            while l < r:
                print(l, r)
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k = k % len(nums)
        _rotate(nums, 0, len(nums) - 1)
        _rotate(nums, 0, k - 1)
        _rotate(nums, k, len(nums) - 1)

        