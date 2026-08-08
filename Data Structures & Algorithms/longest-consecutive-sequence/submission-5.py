class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        curr = 1
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            
            if nums[i] == nums[i - 1] + 1:
                curr += 1

            else:
                curr = 1
            
            streak = max(streak, curr)

            

        return streak
        
        

        
        




        

            
            
            



            
            
