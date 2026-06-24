class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums) + 1)]
        count = {}

        for number in nums:
            count[number] = 1 + count.get(number, 0)
        
        for number, amount in count.items():
            res[amount].append(number)

        output = []

        for i in range(len(res) - 1, 0, -1):
            for j in res[i]:
                output.append(j)
                if len(output) == k:
                    return output
