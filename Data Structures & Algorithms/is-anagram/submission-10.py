class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0 for i in range(26)]

        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a');
            count_s[char_index] += 1;
        
        for i in range(len(t)):
            char_index = ord(t[i]) - ord('a');
            count_s[char_index] -= 1;

        return all(v == 0 for v in count_s)
        

