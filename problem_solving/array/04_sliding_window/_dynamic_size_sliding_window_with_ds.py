
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
output:
123
 234
  345
   456
    567
     678
      789
"""
# output:


# def find_subarray(arr, k):
#     l = 0
#     n = len(arr)+1
#     for r in range(k, n):
#         print(arr[l:r])
#         l += 1
        
# find_subarray(arr, 4)
    
    
# dic = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
# def find_subarray(dic, k):
#     l = 1
#     for r in range(k+1, len(dic)+1):
#         print(dic[l:r])
#         l += 1

# find_subarray(dic, 3)


def max_fixed_subarray(arr, k):
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    n = len(arr)
     # Initialize the sum of the first 'k' elements
    max_sum = sum(arr[:k]) # 4+2+1 = 7
    current_sum = max_sum # 7

    # Initialize two pointers
    l = 0

    # Slide the window across the array
    for r in range(k, n):
        current_sum += arr[r] - arr[l]
        max_sum = max(max_sum, current_sum)
        l += 1
    
    return max_sum

# print(max_fixed_subarray([4,2,1,7,8,1,2,8,1,0], 3))


def min_fixed_subarray(arr, k):
    l = 0
    n = len(arr)
    min_value = sum(arr[:k])
    current_window_sum = min_value
    for r in range(k, n):
        current_window_sum += arr[r] - arr[l]
        min_value = min(min_value, current_window_sum)
        print(arr[l:r], min_value)
        l += 1
    return min_value
print(min_fixed_subarray([1,2,3,-4,5,6,7,8,9], 3))