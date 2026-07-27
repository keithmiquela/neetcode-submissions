class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left=0
        max_right=0
        left=0
        right=len(height)-1
        total_area=0
        while right>=left:
            if max_left<=max_right:
                total_area+=min(max_left,max_right)-height[left] if min(max_left,max_right)-height[left]>0 else 0
                max_left=max(max_left,height[left])
                left+=1
            else:
                total_area+=min(max_left,max_right)-height[right] if min(max_left,max_right)-height[right]>0 else 0
                max_right=max(max_right,height[right])
                right-=1
        return total_area


        

        