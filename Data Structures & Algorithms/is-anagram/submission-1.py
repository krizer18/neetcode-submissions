class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = sorted(s)
        s2 = sorted(t)
        for i, l in enumerate(s1):
            if l != s2[i]:
                return False
        return True