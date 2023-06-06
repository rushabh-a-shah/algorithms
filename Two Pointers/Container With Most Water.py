class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxWater = 0

        while l < r:
            newWater = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, newWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
