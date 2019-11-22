def rotate_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(row, len(matrix[row])):
            print(row, col, col, row)
            swap(matrix, row, col, col, row)
    return matrix


def swap(matrix, r1, c1, r2, c2):
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]


if __name__ == '__main__':
    print(rotate_matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
