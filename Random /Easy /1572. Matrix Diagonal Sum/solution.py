class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        length_of_matrix = len(mat)
        for i in range(length_of_matrix):
            sum += mat[i][i]+mat[i][length_of_matrix-1-i]
        if length_of_matrix%2 !=0:
            sum -= mat[length_of_matrix//2][length_of_matrix//2]
        return sum
