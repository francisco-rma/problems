class TimeMap:
    store: dict[str, list[tuple[int, str]]]  # tuples of (index, value)

    def __init__(self):
        self.store = {}
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        if self.store[key][-1][0] <= timestamp:
            return self.store[key][-1][1]

        values = self.store[key]

        left = 0

        right = len(values) - 1

        while left <= right:
            midpoint = left + ((right - left) // 2)

            if values[midpoint][0] <= timestamp and values[midpoint + 1][0] > timestamp:
                return values[midpoint][1]

            elif values[midpoint][0] < timestamp:
                left = midpoint + 1

            else:
                right = midpoint - 1

        return ""


results = []

timeMap = TimeMap()

results.append(timeMap)

results.append(timeMap.set("test", "one", 10))
results.append(timeMap.set("test", "two", 20))
results.append(timeMap.set("test", "three", 30))
results.append(timeMap.get("test", 15))
results.append(timeMap.get("test", 25))
results.append(timeMap.get("test", 35))
