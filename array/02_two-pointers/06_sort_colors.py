"""
75. Sort Colors
Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    T: O(n)
    S: O(1)
    """
    l, curr, r = 0, 0, len(nums)-1
    
    while curr <= r:
        if nums[curr] == 0:
            nums[l], nums[curr] = nums[curr], nums[l]
            l += 1
            curr += 1
        elif nums[curr] == 1:
            curr += 1
        else:
            nums[curr], nums[r] = nums[r], nums[curr]
            r -= 1
    
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)  # [0,0,1,1,2,2]
    
    nums = [2,0,1]
    sortColors(nums)
    print(nums)  # [0,1,2]