
def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
    
    
if __name__ == '__main__':
    matrix = [ [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print(rotate_matrix(matrix))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]