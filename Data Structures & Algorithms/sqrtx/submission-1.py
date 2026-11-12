class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, max(1, x // 2)

        while l <= r:
            m = (l + r) // 2

            if m ** 2 == x:
                return m
            elif  m ** 2 < x:
                l = m + 1
            else:
                r = m - 1
        
        return r
        