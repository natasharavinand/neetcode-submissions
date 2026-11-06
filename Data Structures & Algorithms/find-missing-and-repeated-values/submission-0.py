class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        valueSet = set()
        result = [-1, -1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in valueSet:
                    result[0] = grid[i][j]
                valueSet.add(grid[i][j])
        

        for n in range(1, len(grid) ** 2 + 1):
            if n not in valueSet:
                result[1] = n
                return result
    
        


        