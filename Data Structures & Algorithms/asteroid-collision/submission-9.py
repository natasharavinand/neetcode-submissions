class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def same_sign(num1, num2):
            return (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0)

        stack = []

        for asteroid in asteroids:
            if not stack or same_sign(asteroid, stack[-1]) or (stack[-1] < 0 and asteroid > 0):
                stack.append(asteroid)
            else:
                if abs(stack[-1]) > abs(asteroid):
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                else:
                    while stack and not same_sign(asteroid, stack[-1]) and abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                    
                    if not stack or same_sign(asteroid, stack[-1]):
                        stack.append(asteroid)
                    elif not same_sign(asteroid, stack[-1]):
                        if abs(asteroid) == abs(stack[-1]):
                            stack.pop()
    
        return stack

        