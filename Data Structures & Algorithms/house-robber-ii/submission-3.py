class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.house1(nums[1:]), self.house1(nums[:-1]))
        

    def house1(self, amount):
        if len(amount) == 0:
            return 0
        if len(amount) <= 2:
            return max(amount)
        
        dp = [0] * len(amount)
        dp[0] = amount[0]
        dp[1] = max(amount[0], amount[1])

        for i in range(2, len(amount)):
            dp[i] = max(dp[i - 2] + amount[i], dp[i - 1])

        return dp[-1]






        