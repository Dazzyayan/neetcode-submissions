from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # tup 0 = timestamp, 1 = value
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        if len(lst) == 0:
            return ""

        l, r = 0, len(lst) - 1

        while l <= r:
            m = (l + r) // 2
            if lst[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        # print(lst)
        bnd = lst[l - 1]
        if bnd[0] <= timestamp:
            return bnd[1]
        else:
            return ""
        
        
