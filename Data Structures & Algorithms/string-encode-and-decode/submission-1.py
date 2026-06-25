class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i + "~"
        return s
    def decode(self, s: str) -> List[str]:
        cur = ""
        res = []
        for i in s:
            if i != '~':
                cur += i
            else:
                res.append(cur)
                cur = ""
        return res
