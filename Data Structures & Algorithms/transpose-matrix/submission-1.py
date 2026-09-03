class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                 k = matrix[i][j] 
                 matrix[i][j] = matrix[j][i]
                 matrix[j][i] = k

        return matrix
