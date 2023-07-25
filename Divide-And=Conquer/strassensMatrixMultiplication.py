def split_matrix(matrix):
    # Split a matrix into four equal-sized submatrices
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen_matrix_multiply(A, B):
    # Base case: if the matrices are 1x1, do regular matrix multiplication
    if A.shape == (1, 1):
        return A * B

    # Split matrices into four submatrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursive calls to calculate seven products (P1 to P7)
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Calculate the four quadrants of the result matrix using the P values
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine the four quadrants to form the final result matrix
    result_matrix = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result_matrix

# Example usage
import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

B = np.array([[17, 18, 19, 20],
              [21, 22, 23, 24],
              [25, 26, 27, 28],
              [29, 30, 31, 32]])

result = strassen_matrix_multiply(A, B)
print(result)
