class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
            if not stack:
                stack.append(time)
            else:
                cur = stack[-1]
                if time <= cur:
                    pass
                else:
                    stack.append(time)
        return len(stack)


            
            


