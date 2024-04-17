"""
47. Permutations II

Medium
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

def permuteUnique(nums):
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
            if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
                continue
            if visited[i]:
                continue
            visited[i] = True
            path.append(num)
            # explore
            backtrack(path=path)
            # deselect
            path.pop()
            visited[i] = False
            
    ans = []
    visited = [False] * len(nums)
    nums.sort()
    backtrack(path=[])
    return ans
    
if __name__ == '__main__':
    nums = [1,1,2]
    print(permuteUnique(nums))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    nums = [1,2,3]
    print(permuteUnique(nums))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]