
def is_anagram(arr, size):
    """
    [1,2,3,4], 2 => [[1,2], [3,4]]
    [1,2,3,4,5], 3 => [[1,2], [3,4], [5]]
    """
    ans = []
    for i in range(0, len(arr), size):
        ans.append(arr[i:i+size])
    
    return ans


if __name__ == "__main__":
    print(is_anagram([1, 2, 3, 4, 5], 3))