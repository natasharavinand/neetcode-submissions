class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        seen = set()
        maxLength = 0

        for window_end in range(len(s)):
            while s[window_end] in seen:
                seen.remove(s[window_start])
                window_start += 1
            
            seen.add(s[window_end])
            
            maxLength = max(maxLength, len(seen))
        
        return maxLength
        