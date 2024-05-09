"""
216. Combination Sum III
Medium

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used. Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.


Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 
 
Constraints:
2 <= k <= 9
1 <= n <= 60
"""

def combinationSumIII(k, n):
    """
    Time complexity: O(9^k)
    Space complexity: O(k)
    result => 9^k combinations
    """
    def backtrack(index, path, target):
        # if meet the condition
        if target == 0 and len(path) == k:
            ans.append(path[:])
            return
        # for selection in selections
        for i in range(index, len(nums)):
            # select
            num = nums[i]
            if num > target:
                continue
            path.append(num)
            # explore
            backtrack(index=i+1, path=path, target=target-num)
            # deselect
            path.pop()
            
    ans = []
    nums = list(range(1, 10))
    backtrack(index=0, path=[], target=n)
    return ans

if __name__ == '__main__':
    k = 3
    n = 7
    print(combinationSumIII(k, n))  # [[1, 2, 4]]
    k = 3
    n = 9
    print(combinationSumIII(k, n))  # [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    k = 4
    n = 1
    print(combinationSumIII(k, n))  # []
