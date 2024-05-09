def find_sum_of_three(nums, target):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    nums.sort()
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            
            if total == target:
                return True
            elif total < target:
                l += 1
            else:
                r -= 1
            
    return False

if __name__ == "__main__":
    print(find_sum_of_three([2, 3, 4, 5, 7, 8, 9], 20))  # True
    print(find_sum_of_three([2, 3, 4, 5, 7, 8, 9], 101))  # False
    print(find_sum_of_three([2, 3, 4, 5, 7, 8, 9], 22))  # True