# def zero_matrix(matrix):  # O(N^2*M^2)
#     cols_modified = {}
#     for row_idx, row in enumerate(matrix):
#         for col_idx in range(len(row)):
#             if row[col_idx] == 0 and not cols_modified.get(col_idx, False):
#                 matrix[row_idx] = [0 for _ in range(len(row))]
#                 for row2 in range(len(matrix)):
#                     matrix[row2][col_idx] = 0
#                 cols_modified[col_idx] = True
#
#     return matrix

def zero_matrix(matrix):  # O(N*M + A*B*N) --> O(N(M + AB))
    points = {}
    for row_idx, row in enumerate(matrix):  # N * M
        for col_idx in range(len(row)):
            if row[col_idx] == 0 and col_idx not in points.get(row_idx, []):
                points[row_idx] = points.get(row_idx, [])
                points[row_idx].append(col_idx)

    for row, columns in points.items():  # A --> rows with zeros
        matrix[row] = [0 for _ in range(len(matrix[row]))]
        for col in columns:  # --> B cols with zeros
            for row2 in range(len(matrix)):  # N
                matrix[row2][col] = 0
    return matrix


if __name__ == '__main__':
    print(zero_matrix([[1, 2, 3, 0], [1, 2, 3, 4]]))
    print(zero_matrix([[1, 2, 0, 0], [1, 2, 3, 4]]))
    print(zero_matrix([[1, 0, 0, 0], [1, 2, 3, 4]]))

    # print([[0 for _ in range(10)] for _ in range(10)])
