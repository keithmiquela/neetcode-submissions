class Solution:
    def maxArea(self, heights: List[int]) -> int:
        prev_i=0
        max_volume=0
        i=0
        while i < len(heights)-1:
            if heights[i]>prev_i:
                j=len(heights)-1
                prev_j=0
                while j > i:
                    if heights[j] > prev_j:
                        max_volume = max(max_volume,(j-i)*min(heights[i],heights[j]))
                        if heights[j]>=heights[i]:
                            break
                        prev_j=heights[j]
                    j-=1
            i+=1
        return max_volume


