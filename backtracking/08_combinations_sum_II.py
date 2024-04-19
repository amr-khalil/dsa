"""
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

def combinationSumII(candidates, target):
    """
    Time complexity: O(n^m)
    Space complexity: O(m)
    result => n^m combinations
    """
    def backtrack(index, path, target):
        # if meet the condition
        if target == 0:
            ans.append(path[:])
            return
        # for selection in selections
        for i in range(index, len(candidates)):
            # select
            num = candidates[i]
            # if the number is greater than the target, skip
            if num > target:
                continue
            # if the number is the same as the previous number, skip
            if i > index and candidates[i] == candidates[i-1]:
                continue
            path.append(num)
            # explore
            backtrack(index=i+1, path=path, target=target-num)
            # deselect
            path.pop()
            
    ans = []
    candidates.sort()
    backtrack(index=0, path=[], target=target)
    return ans


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSumII(candidates, target))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    candidates = [2,5,2,1,2]
    target = 5
    print(combinationSumII(candidates, target))  # [[1, 2, 2], [5]]
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 8
    print(combinationSumII(candidates, target))  # [[1, 1, 1, 1, 1, 1, 1, 1]]
