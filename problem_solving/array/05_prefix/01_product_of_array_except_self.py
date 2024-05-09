"""
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that 
- runs in **O(n)** time and
- without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

def productExceptSelf1(nums):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    n = len(nums)
    ans = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                ans[i] *= nums[j]
    return ans

def productExceptSelf2(nums):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    n = len(nums)
    left = [1] * n
    right = [1] * n
    ans = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(n):
        ans[i] = left[i] * right[i]
    return ans

def productExceptSelf(nums):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    n = len(nums)
    ans = [1] * n
    for i in range(1, n):
        ans[i] = nums[i-1] * ans[i-1]
            
    product = 1
    for i in range(n-1, -1, -1):
        ans[i] *= product
        product *= nums[i]
    return ans

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
    print(productExceptSelf([1,2,3,4,5])) # [120,60,40,30,24]