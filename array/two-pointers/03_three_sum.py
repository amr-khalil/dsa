"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(nums):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # array
    # sort array
    nums.sort()
    ans = []
    target = 0
    for i in range(0, len(nums)-2):
        # reset pointer => l=i+1
        l, r = i+1, len(nums)-1
        # i=0, use another while loop
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target and (i != l and i != r and l != r):
                total_list = [nums[i], nums[l], nums[r]]
                total_list.sort()
                if total_list not in ans:
                    ans.append(total_list)
                l += 1
                r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
    
    return ans


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
    print(threeSum([0,1,1]))  # []
    print(threeSum([0,0,0]))  # [[0,0,0]]