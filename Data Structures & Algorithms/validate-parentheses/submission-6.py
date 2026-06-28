class Solution:
    def isValid(self, s: str) -> bool:
        mapdict = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for i in s:
            if i in mapdict:
                if not stack:
                    return False
                bracket = stack.pop()
                if mapdict[i] != bracket:
                    return False
            else:
                stack.append(i)

        if stack:
            return False

        return True
                
