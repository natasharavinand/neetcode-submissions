class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            
            if l < r and s[l].lower() != s[r].lower():
                if self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1):
                    return True
                return False
            
            l += 1
            r -= 1
                
        return True
    
    def isPalindrome(self, s, l, r):
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

        