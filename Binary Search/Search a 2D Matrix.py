class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        row_num = 0
        
        while l <= r:
            m = (l + r)//2
            if matrix[m][0] <= target:
                if matrix[m][-1] >= target:
                    row_num = m
                    break
                else:
                    l = m + 1
            else:
                r = m - 1
        
        row = matrix[row_num]
        l = 0
        r = len(row)-1

        while l <= r:
            m = (l + r)//2
            if row[m] == target:
                return True
            if target > row[m]:
                l = m + 1
            else:
                r = m - 1
        return False
