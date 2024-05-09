"""
90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


def subsetsWithDup(nums):
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    result => 2^n subsets
    """
    def backtrack(index, path):
        # if meet the condition
        if tuple(path) not in seen:
            ans.append(path[:])
            seen.add(tuple(path))

        # for selection in selections
        for i in range(index, len(nums)):
            # select
            num = nums[i]
            path.append(num)
            # explore
            backtrack(index=i+1, path=path)
            # deselect
            path.pop() 
            
    ans = []
    seen = set()
    # sort the nums to avoid duplicates
    nums.sort()
    backtrack(index=0, path=[])
    return ans


if __name__ == '__main__':
    nums = [1,2,2]
    print(subsetsWithDup(nums))  # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    nums = [0]
    print(subsetsWithDup(nums))  # [[], [0]]
    nums = [4,1,4]
    print(subsetsWithDup(nums))  # [[], [1], [1, 4], [1, 4, 4], [4], [4, 4]]
