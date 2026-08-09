class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        total = (nums[0] * nums[1]) - (nums[-1] * nums[-2])
        return abs(total)