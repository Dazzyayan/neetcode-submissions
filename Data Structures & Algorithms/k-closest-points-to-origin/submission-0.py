from heapq import *
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for coords in points:
            tup = (get_distance(coords), coords)
            if len(h) == k:
                heappushpop_max(h, tup)
            else:
                heappush_max(h, tup)
        
        return [tup[1] for tup in h]
    
def get_distance(xy):
    return sqrt(xy[0]**2 + xy[1]**2)