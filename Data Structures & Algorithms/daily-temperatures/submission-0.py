class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # highest = temperatures[0]
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            count = 0
            while len(stack) > 0 and temp > stack[-1][1]:
                # if i > 4:
                    # print(temp, stack, result)
                tup = stack.pop()
                # count += 1
                # print(stack, count)
                result[tup[0]] = i - tup[0]
            
            stack.append((i, temp))
            print(temp, stack, result)
            
        return result