class Solution:
    def countSubstrings(self, s: str) -> int:
        palin_number = 0

        for i in range(len(s)):

            ##odd check
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin_number += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin_number += 1
                l -= 1
                r += 1
        return palin_number
