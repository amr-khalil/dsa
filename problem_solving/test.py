

def binary_search(arr, target):
    """
    binary search
    time complexity: O(logn)
    space complexity: O(1)
    """
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return r


def nearst_pos(locations, target):
    """
    find the nearest number to the target
    time complexity: O(n)
    space complexity: O(1)
    """
    nearest = binary_search(locations, target)
    return nearest
    

target = 85
locations = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nearst_pos(locations, target)) # 5