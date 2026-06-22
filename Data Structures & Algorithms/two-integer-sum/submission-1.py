class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mydic:
                return [mydic[complement], i]
            else:
                mydic[n] = i
        