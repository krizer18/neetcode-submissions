class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        l, r = 0, 0
        maxfreq = 0
        maxlen = 0

        while r < len(s): 
            count_dict[s[r]] = 1 + count_dict.get(s[r], 0)
            maxfreq = max(maxfreq, count_dict[s[r]])

            while (r - l + 1) - maxfreq > k:
                count_dict[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

            r += 1

        return maxlen