class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]
        water = 0

        while l < r:
            if maxL < maxR:
                # shift left pointer
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]
            else:
                # shift right pointer
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        
        return water
