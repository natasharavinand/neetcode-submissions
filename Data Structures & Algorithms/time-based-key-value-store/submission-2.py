class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
            
        return values[r][0] if values[r][1] <= timestamp else ""
        

