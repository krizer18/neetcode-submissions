class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newlist = sorted(list(set(nums)))
        print(newlist)
        hashset = set()
        longest = 0
        for i, n in enumerate(newlist):
            if not hashset:
                hashset.add(n)
            elif hashset and (n - 1 == newlist[i - 1]):
                hashset.add(n)
            else:
                longest = max(longest, len(hashset))
                hashset.clear()
                hashset.add(n)
        if hashset:
            longest = max(longest, len(hashset))
        return longest

            

