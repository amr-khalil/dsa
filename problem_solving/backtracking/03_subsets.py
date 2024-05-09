"""
78. Subsets

Medium

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


def subsets(nums):
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    result => 2^n subsets
    """
    ans = []
    def backtrack(index, path):
        # if meet the condition
        ans.append(path[:])
        # for selection in selections
        for i in range(index, len(nums)):
            # select
            num = nums[i]
            path.append(num)
            # explore
            backtrack(index=i+1, path=path)
            # deselect
            path.pop()
            
    backtrack(index=0, path=[])
    return ans

if __name__ == '__main__':
    nums = [1,2,3]
    print(subsets(nums))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    nums = [0]
    print(subsets(nums))  # [[], [0]]
    nums = [1,2,3,4]
    print(subsets(nums))  # [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]
