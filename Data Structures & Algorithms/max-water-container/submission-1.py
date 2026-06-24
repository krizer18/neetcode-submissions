class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxa = max(maxa, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxa



                