"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

def permute(nums):
    """
    Time complexity: O(n!)
    Space complexity: O(n!)
    result => n! permutations
    HINT: In the permutation the order of the elements matters!
    """
    
    def backtrack(path):
        # if meet the condition
        if len(path) == len(nums):
            ans.append(path[:])
            return
        # for selection in selections
        for i in range(len(nums)):
            # select
            num = nums[i]
            # filter out the visited numbers
            if num in path:
                continue
            path.append(num)
            # explore
            backtrack(path=path)
            # deselect
            path.pop()
            
    ans = []
    backtrack(path=[])
    return ans


if __name__ == '__main__':
    nums = [1,2,3]
    print(permute(nums))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    nums = [0,1]
    print(permute(nums))  # [[0, 1], [1, 0]]
    nums = [1]
    print(permute(nums))  # [[1]]