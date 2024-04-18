"""
39. Combination Sum

Medium

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

def combinationSum(candidates, target):
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
            if num > target:
                continue
            path.append(num)
            # explore
            backtrack(index=i, path=path, target=target-num)
            # deselect
            path.pop()
            
    ans = []
    backtrack(index=0, path=[], target=target)
    return ans

def combinationSum2(candidates, target):
    """
    Time complexity: O(n^m)
    Space complexity: O(m)
    result => n^m combinations
    """
     
    def backtrack(path):
        # condition
        if sum(path) == target and tuple(sorted(path)) not in seen:
            ans.append(path[:])
            seen.add(tuple(path))
            return 
        
        # for select in selections
        for i in range(len(candidates)):
            # select
            num = candidates[i]
            if num + sum(path) > target:
                continue
            path.append(num)
            # explore
            backtrack(path=path)
            # deselect
            path.pop()
    
    seen = set()
    candidates.sort()
    ans = []
    backtrack(path=[])
    return ans

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates, target))  # [[2, 2, 3], [7]]
    candidates = [2,3,5]
    target = 8
    print(combinationSum(candidates, target))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    candidates = [2]
    target = 1
    print(combinationSum(candidates, target))  # []
    candidates = [8,7,4,3]
    target = 7
    print(combinationSum(candidates, target))  # [[3, 4], [7]]
