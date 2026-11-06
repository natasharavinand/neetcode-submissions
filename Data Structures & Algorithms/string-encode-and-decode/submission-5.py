class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            n = len(s)
            result.append(f"{n}!{s}")
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        
        while i < len(s):
            separator_idx = s.find("!", i)
            length = int(s[i:separator_idx])
            word_start = separator_idx + 1 # skip separator
            word = s[word_start:word_start + length]
            result.append(word)
            i = word_start + length

        return result





