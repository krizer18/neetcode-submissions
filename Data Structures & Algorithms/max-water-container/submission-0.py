class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        greatest = 0
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            greatest = max(greatest, water)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                l += 1
        return greatest

