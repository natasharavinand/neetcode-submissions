class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []

        for op in operations:
            print(points)
            if op.removeprefix("-").isdigit():
                points.append(int(op))
            else:
                if op == "+":
                    points.append(points[-2] + points[-1])
                elif op == "D":
                    points.append(points[-1] * 2)
                else:
                    points.pop()
        
        return sum(points)