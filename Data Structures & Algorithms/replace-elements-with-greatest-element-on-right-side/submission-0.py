class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxFromRight = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = maxFromRight
            maxFromRight = max(maxFromRight, tmp)
        
        return arr
        