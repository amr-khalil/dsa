import matplotlib.pyplot as plt

def invert_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # traverse the matrix
    for r in range(rows):
        for c in range(cols):
            # invert the value
            matrix[r][c] = 1 - matrix[r][c]
    return matrix



if __name__ == '__main__':
    # create 64 x 64 image with random values
    image = [[0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]

    image = invert_matrix(image)
    
    # draw 64 x 64 image
    plt.imshow(image, cmap='gray')
    # display image
    plt.show()