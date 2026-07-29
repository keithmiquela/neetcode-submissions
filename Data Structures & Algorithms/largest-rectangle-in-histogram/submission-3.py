class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialize the stack
        stack = []

        # link heights with indices
        rectangles = [[heights[i], i] for i in range(len(heights))]
        # rectangles[0] = height
        # rectangles[1] = index

        # return value
        max_area = 0

        # helper method: findArea(height, index_a, index_b)
            # width = index_b - index_a
            # return width * height
        def findArea(height, i, j):
            width = j - i
            return width * height

        # loop through heights
        for i in range(len(rectangles)):
            rect = rectangles[i]
            # if not stack, add
            if not stack:
                stack.append(rect)
                continue

            # if curr_height > prev_height, then add to stack
            curr_height = rect[0]
            prev_rect = stack[-1]
            prev_height = prev_rect[0]

            if curr_height > prev_height:
                stack.append(rect)
                continue
            else:
                index = rect[1]
                temp_index = index
                while curr_height <= prev_height:
                    prev_index = prev_rect[1]
                    max_area = max(max_area, findArea(prev_height, prev_index, index))
                    temp_index = prev_index 
                    # bug?

                    stack.pop()
                    if not stack:
                        break

                    prev_rect = stack[-1]
                    prev_height = prev_rect[0]

                rect[1] = temp_index
                stack.append(rect)
            
        # loop through stack
            # curr_area = findArea(height, index, n)
            # max_area = max(max_area, curr_area)
        for rect in stack:
            height = rect[0]
            index = rect[1]

            area = findArea(height, index, len(rectangles))
            max_area = max(max_area, area)
        
        # return max_area
        return max_area
                
        
        
