import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile("[^a-zA-Z0-9]")
        print(s)
        s = regex.sub("", s)
        print(s)
        s = s.replace(" ", "")
        s = s.lower()
        print(s)

        left = 0
        right = len(s) - 1 
        while left <= right:
            if s[left] == s[right]:
                print(f"left={s[left]}, right={s[right]}")
                left += 1
                right -= 1
            else:
                return False
        
        return True