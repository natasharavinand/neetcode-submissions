class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []

        for letter_idx in range(len(strs[0])):
            for str_idx in range(len(strs)):
                current_str = strs[str_idx]
                if letter_idx == len(current_str):
                    return ''.join(lcp) # out of bounds for shortest string
                if strs[0][letter_idx] != strs[str_idx][letter_idx]:
                    return ''.join(lcp) # first mismatch
            lcp.append(strs[0][letter_idx])
        
        return ''.join(lcp)
        