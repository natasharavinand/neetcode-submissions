class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        result = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            result[(i + k) % len(nums)] = nums[i]
        
        nums[:] = result
        






        # k 

        # 1,2,3,4,5,6,7,8

      


        # 8,1,2,3,4,5,6,7 1
        # 7,8,1,2,3,4,5,6 2 
        # 6,7,8,1,2,3,4,5 3 
        # 5,6,7,8,1,2,3,4 4
        # 4,5,6,7,8,1,2,3 5 
        

        