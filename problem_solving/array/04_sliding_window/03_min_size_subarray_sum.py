"""
209. Minimum Size Subarray Sum
Medium
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

steps:
nums = [2,3,1,2,4,3]
l: 0, r: 0, sum: 2
l: 0, r: 1, sum: 5
l: 0, r: 2, sum: 6
l: 0, r: 3, sum: 8
l: 0, r: 3, sum: 8, window_size: 4, ans: 4
l: 1, r: 4, sum: 10
l: 1, r: 4, sum: 10, window_size: 4, ans: 4
l: 2, r: 4, sum: 7, window_size: 3, ans: 3
l: 3, r: 5, sum: 9
l: 3, r: 5, sum: 9, window_size: 3, ans: 3
l: 4, r: 5, sum: 7, window_size: 2, ans: 2
"""


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    Time complexity: O(n)
    Space complexity: O(1)
    """
    ans = float('inf')
    sum = 0
    l = 0
    for r in range(len(nums)):
        sum += nums[r]
        print(f"l: {l}, r: {r}, sum: {sum}")
        while sum >= target:
            window_size = r - l + 1
            ans = min(ans, window_size)
            print(f"l: {l}, r: {r}, sum: {sum}, window_size: {window_size}, ans: {ans}")
            sum -= nums[l]
            l += 1
        
        


if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    print(minSubArrayLen(target, nums))  # 2
    target = 4
    nums = [1,4,4]
    print(minSubArrayLen(target, nums))  # 1
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(minSubArrayLen(target, nums))  # 0