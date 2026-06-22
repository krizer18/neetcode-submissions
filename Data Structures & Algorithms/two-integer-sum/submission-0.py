class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in res:
                return [res[need], i]
            else:
                res[n] = i



