class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for d, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                poppedTemp, poppedDay = stack.pop()
                result[poppedDay] = d - poppedDay

            stack.append((t, d))

        return result