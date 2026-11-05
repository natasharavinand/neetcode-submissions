class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            t_dict[t[i]] += 1

        if len(s_dict) != len(t_dict):
            return False
        
        for char, freq in s_dict.items():
            if (char not in t_dict) or (t_dict[char] != freq):
                return False
        
        return True
            
        

    