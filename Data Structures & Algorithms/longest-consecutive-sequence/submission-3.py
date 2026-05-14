from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        longest = 0
        seen = set()

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            for side in (-1, 0, 1):
                d[num + side] +=1
        print(d)
        for key in d:
            if d[key] == 2:
                i = 1
                count = 1
                dir = 1 if d[key + 1] == 3 else - 1

                strlist = []
                while d[key + dir * i] == 3:
                    count += 1
                    i += 1
                    strlist.append(key + dir * i)
                
                if d[key + dir * i] == 2:
                    count += 1

                if count > longest:
                    longest = count
                    long_s = str(strlist)
                    print("longest so far", long_s)
                # longest = count if count > longest else longest
                # long_s = str(strlist) if count > longest else long_s

        if len(seen) == 1:
            return 1
        
        return longest


        