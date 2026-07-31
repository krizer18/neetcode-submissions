class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        myset = set()
        def backtrack(curr, i):
            if curr not in myset:
                output.append(list(curr))
            
            for j in range(i, len(nums)):
                if curr in myset:
                    continue
            
                currlist = list(curr)
                currlist.append(nums[j])
                curr = tuple(currlist)
                backtrack(curr, j + 1)
                curr = list(curr)
                curr.pop()
                curr = tuple(curr)
        backtrack((), 0)
        return output
