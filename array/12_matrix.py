
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
if __name__ == "__main__":
    matrix(3)