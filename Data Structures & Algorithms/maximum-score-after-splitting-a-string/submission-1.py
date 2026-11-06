class Solution:
    def maxScore(self, s: str) -> int:  
        maxResult = 0

        for i in range(len(s) - 1):
            left = s[:i+1].count("0")
            right = s[i+1:].count("1")
            count = left + right
            maxResult = max(count, maxResult)
        
        return maxResult
        