class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0
        while j>i:
            min_height = min(heights[i],heights[j])
            max_area = max(min_height*(j-i), max_area)
            if heights[i]==min_height:
                i+=1
            else:
                j-=1
        return max_area