class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        def calcRect(beginning, end):
            width = end - beginning[0]
            height = beginning[1]
            return width * height

        for i in range(0, len(heights)):
            if len(stack) == 0:
                stack.append([i,heights[i]])
                continue
            curr_height = heights[i]
            prev_height = stack[-1][1]

            if curr_height > prev_height:
                stack.append([i,curr_height])
                continue
            elif curr_height == prev_height:
                continue
            while curr_height < prev_height:
                max_area = max(calcRect(stack[-1], i),max_area)
                old_beg = stack.pop()[0]
                if len(stack) == 0:
                    break
                prev_height = stack[-1][1]
            stack.append([old_beg,heights[i]])

        
        while len(stack)>0:
            max_area = max(calcRect(stack[-1], len(heights)),max_area)
            stack.pop()
        return max_area


