class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        myset = set()
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                tsum = n + nums[l] + nums[r]
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    myset.add(tuple([n, nums[l], nums[r]]))
                    l += 1
                    r -= 1
        return list(myset)
            

