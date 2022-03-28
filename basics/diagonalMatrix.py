def takeInput():
    matrix_length = int(input('Enter length of array:'))


def diagonalSubtraction(grid):
    matrix_length = len(grid)
    left_diagonal_sum, right_diagonal_sum = 0, 0
    for i in range(matrix_length):
        for j in range(matrix_length):
            if(i == j):
                left_diagonal_sum += grid[i][j]
            elif(i + j == matrix_length - 1):
                right_diagonal_sum += grid[i][j]

    return left_diagonal_sum - right_diagonal_sum


grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 15]]


diagonal_subtraction_result = diagonalSubtraction(grid)

print('The subtraction is: ', diagonal_subtraction_result)
