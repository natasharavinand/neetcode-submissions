class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
        
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s2_count[i] == s1_count[i]:
                matches += 1
        
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            if s2_count[(ord(s2[i - len(s1)]) - ord('a'))] == s1_count[(ord(s2[i - len(s1)]) - ord('a'))]:
                matches -= 1
            s2_count[(ord(s2[i - len(s1)]) - ord('a'))] -= 1
            if s2_count[ord(s2[i - len(s1)]) - ord('a')] == s1_count[ord(s2[i - len(s1)]) - ord('a')]:
                matches += 1
            
            if s2_count[ord(s2[i]) - ord('a')] == s1_count[ord(s2[i]) - ord('a')]:
                matches -= 1
            s2_count[ord(s2[i])- ord('a')] += 1
            if s2_count[ord(s2[i]) - ord('a')] == s1_count[ord(s2[i]) - ord('a')]:
                matches += 1

            if matches == 26:
                return True
        
        return False

