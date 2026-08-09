class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur = 0
        for i in logs:
            if i == "../":
                if cur == 0:
                    continue
                else:
                    cur -= 1
            elif i == "./":
                continue
            else:
                cur += 1
        return cur