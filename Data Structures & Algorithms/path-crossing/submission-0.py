class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mypositions = []
        position = [0, 0]
        mypositions.append(position.copy())

        for i in path:
            if i == 'N':
                position[0] += 1
            elif i == 'S':
                position[0] -= 1
            elif i == 'E':
                position[1] += 1
            elif i == 'W':
                position[1] -= 1
        
            if position in mypositions:
                return True

            else:
                mypositions.append(position.copy())
        
        return False



