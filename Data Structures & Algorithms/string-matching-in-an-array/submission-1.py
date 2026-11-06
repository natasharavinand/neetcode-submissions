class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()

        for i, word in enumerate(words):
            for j in range(len(words)):
                if i == j: continue
                if word in words[j]:
                    result.add(word)
        
        return list(result)
