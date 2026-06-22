class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mydict:
                return[mydict[complement], i]
            else:
                mydict[n] = i
        
            