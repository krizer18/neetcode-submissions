class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(i, cur, total):
            if total == target:
                output.append(cur.copy())
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    continue
                cur.append(nums[j])
                backtrack(j, cur, total + nums[j])
                cur.pop()
        backtrack(0, [], 0)
        return output

          



