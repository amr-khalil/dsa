
def matrix(n):
    """
    n = 3, matrix:
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
    """
    ans = []
    count = 0
    for r in range(n):
        row = []
        for c in range(n):
            row.append(count)
            count += 1
        ans.append(row)
            
    print(ans)

def matrix2(n):
    """
    r*n + c
    0*3 + 0 = 0
    0*3 + 1 = 1
    0*3 + 2 = 2
    1*3 + 0 = 3
    1*3 + 1 = 4
    1*3 + 2 = 5
    2*3 + 0 = 6
    2*3 + 1 = 7
    2*3 + 2 = 8
    """
    ans = [[r*n + c for c in range(n)] for r in range(n)]
    print(ans)

if __name__ == "__main__":
    matrix2(3)
    # ans = [[i*n + j for j in range(n)] for i in range(n)]
    # print(ans)