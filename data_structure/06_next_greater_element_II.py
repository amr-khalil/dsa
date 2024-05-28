"""
503. Next Greater Element II
Medium
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

def nextGreaterElementII(nums: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = []
    dic = {}
    n = 2*len(nums)
    for i in range(n):
        idx = i%len(nums)
        while stack and nums[stack[-1]] < nums[idx]:
            dic[stack.pop()] = nums[idx]
        stack.append(idx)
        
    return [dic.get(i, -1) for i in range(len(nums))]

if __name__ == '__main__':
    nums = [1,2,1]
    print(nextGreaterElementII(nums)) # [2,-1,2]
    nums = [1,2,3,4,3]
    print(nextGreaterElementII(nums)) # [2,3,4,-1,4]