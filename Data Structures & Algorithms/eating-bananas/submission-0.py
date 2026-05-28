from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        total = sum(piles)

        def calcHrs(pl, k):
            tot = 0
            for item in pl:
                tot += ceil(item / k)
            return tot
        
        k = high
        while low <= high:
            mid = (high + low) // 2
            hrs = calcHrs(piles, mid)
            if hrs <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return k
            
        

