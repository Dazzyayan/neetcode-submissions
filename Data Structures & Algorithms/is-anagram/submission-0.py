class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for letter in s:
            if map.get(letter):
                map[letter] += 1
            else:
                map[letter] = 1
        
        for letter in t:
            if not map.get(letter):
                return False
            else:
                map[letter] +=1
        
        for value in map.values():
            if value % 2 != 0:
                return False
        
        return True