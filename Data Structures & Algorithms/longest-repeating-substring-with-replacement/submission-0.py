# from collections import defaultdict
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         map = defaultdict(int)
#         l = 0
#         r = 0
#         longest = 0
#         count = 0
#         budget = 0

#         while r < len(s):
#             if l == r:
#                 r += 1
#                 count += 1
#                 continue
            
#             if s[r] == s[r - 1 - budget]:
#                 if budget == 0:
#                     map[s[r]] == r
#                 count += 1
#                 r += 1
#                 longest = max(longest, count)
#             elif k - budget > 0:
#                 count += 1
#                 budget += 1
#                 r += 1
#                 longest = max(longest, count)
#             else:
#                 l = map[s[r - 2 - budget]]
#                 r = l 
#                 budget = 0
#                 count = 0

#         return longest
                
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res




