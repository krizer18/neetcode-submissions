class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        row = 0
        rowlen = len(matrix[0]) - 1

        for i in range(0, len(matrix)):
            if matrix[i][rowlen] >= target:
                row = i
                break
            else: 
                pass

        l, r = 0, len(matrix[row]) - 1
        print(row)

        while l <= r:
            mid = l + ((r - l) // 2)
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
        return False
            


