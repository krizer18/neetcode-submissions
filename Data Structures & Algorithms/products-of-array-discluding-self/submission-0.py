class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total = 1
        zero_count = 0

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                total = total * i
        
        for i,n in enumerate(nums):
            if zero_count > 1:
                break
            elif zero_count == 1:
                if n == 0:
                    output[i] = total
            else:
                output[i] = total // n

        
        return output

            