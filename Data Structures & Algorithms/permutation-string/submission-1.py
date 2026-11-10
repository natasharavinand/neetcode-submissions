class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s1_substring_count = {}
        
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        window_start = 0

        for window_end in range(len(s2)):
            if s2[window_end] not in s1_count:
                window_start = window_end + 1
                s1_substring_count = {}
                continue
            
            s1_substring_count[s2[window_end]] = s1_substring_count.get(s2[window_end], 0) + 1

            while s1_substring_count[s2[window_end]] > s1_count[s2[window_end]]:
                s1_substring_count[s2[window_start]] -= 1
                window_start += 1
            
            if s1_substring_count == s1_count:
                return True
        
        return False

            


        