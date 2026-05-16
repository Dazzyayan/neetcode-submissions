class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = "({["
        closes = "]})"
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != pairs[c]:
                    return False
                else:
                    continue
        
        return len(stack) == 0
             
