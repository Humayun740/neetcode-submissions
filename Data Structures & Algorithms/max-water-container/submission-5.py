class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l != r or l < r:
            length = (r+1)-(l+1)
            if heights[r] < heights[l]:
                height = heights[r]
            else:
                height = heights[l]
            currWater = length*height
            if currWater > maxWater:
                maxWater = currWater
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater


        