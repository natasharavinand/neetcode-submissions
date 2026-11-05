class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = {} # sorted: [original_string]

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in sorted_anagrams:
                sorted_anagrams[sorted_s] = []
            sorted_anagrams[sorted_s].append(s)
        
        return [s for s in sorted_anagrams.values()]
