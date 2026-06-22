class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnum = set(nums)
        return not len(nums) == len(newnum)