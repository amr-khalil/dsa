
def mirror_matrix(matrix):
    return [row[::-1] for row in matrix[::-1]] 
    
if __name__ == '__main__':
    matrix = [ [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print(mirror_matrix(matrix))  # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]