
def flip_matrix(matrix):
    return [row[::-1] for row in matrix]


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(flip_matrix(matrix))  # [[3, 2, 1],[6, 5, 4], [9, 8, 7]]