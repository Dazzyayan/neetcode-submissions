import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq.heapify_max(stones)

        while len(stones) > 1:
            x = hq.heappop_max(stones)
            y = hq.heappop_max(stones)

            if x == y:
                continue
            else:
                hq.heappush_max(stones, abs(x - y))
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
