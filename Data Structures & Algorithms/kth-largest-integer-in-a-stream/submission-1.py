import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.h = nums

        while len(self.h) > self.k:
            heapq.heappop(self.h)
        
    def add(self, val: int) -> int:
        if len(self.h) == self.k:
            heapq.heappushpop(self.h, val)
        else:
            heapq.heappush(self.h, val)
        
        return self.h[0]
        
