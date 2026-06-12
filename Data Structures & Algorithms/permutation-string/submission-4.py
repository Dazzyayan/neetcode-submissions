# def get_ind(char):
#     return ord(char) - ord('a')

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         id = [0] * 26
#         for char in s1:
#             id[get_ind(char)] += 1
#         id = tuple(id)

#         l = 0
#         wid = [0] * 26
#         last_seen = [0] * 26
#         for r in range(0, len(s2)):
#             if len(s2[l:r]) == len(s1):
#                 print("true", s2[l:r])
#                 return True

#             char = s2[r]
#             i = get_ind(char)
#             if id[i] > 0:
#                 wid[i] += 1
#                 last_seen[i] = r
#                 if wid[i] > id[i]:
#                     print("w", wid[i], "id", id[i], "char", char)
#                     print(s2[l:r])
#                     l = last_seen[i] + 1
#                     wid[i] -= 1
#             else:
#                 print("w", wid[i], "id", id[i], "char", char)
#                 print(s2[l:r])
#                 l = r + 1
#                 wid = [0] * 26
                    
            

#         return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        
