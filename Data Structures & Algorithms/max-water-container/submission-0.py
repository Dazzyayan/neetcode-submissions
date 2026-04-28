class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = right - left
        # height = whichever is smaller
        # track largest area

        max = 0
        # left = 0
        # right = len(heights) - 1
        for i in range(0, len(heights), 1):
            for j in range(i + 1, len(heights), 1):
                h = heights[i] if heights[i] <= heights[j] else heights[j]
                area = (j - i)*h
                # print(area)
                if area > max:
                    max = area
        
        return max