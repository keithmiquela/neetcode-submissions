class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = [0] * len(height)
        temp_max_left = 0
        for i in range(len(height)):
            num = height[i]
            temp_max_left = max(num, temp_max_left)
            max_height[i] = temp_max_left
        
        temp_max_right = 0
        for i in range(len(height)-1, -1, -1):
            num = height[i]
            temp_max_right = max(temp_max_right, num)
            max_height[i] = min(temp_max_right, max_height[i])

        result = 0
        for i in range(0, len(height)):
            result += max_height[i] - height[i]
        return result