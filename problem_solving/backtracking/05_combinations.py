"""
77. Combinations

Medium
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""

def combine(n, k):
    """
    Time complexity: O(n!/(k!(n-k)!))
    Space complexity: O(n!/(k!(n-k)!))
    result => n!/(k!(n-k)!) combinations
    
    HINT: In the combination the order of the elements does not matter!
    """
    
    def backtrack(index, path):
        # if meet the condition
        if len(path) == k:
            ans.append(path[:])
            return
        # for selection in selections
        for i in range(index, n+1):
            # select
            path.append(i)
            # explore
            backtrack(index=i+1, path=path)
            # deselect
            path.pop()
            
    ans = []
    backtrack(index=1, path=[])
    return ans

if __name__ == '__main__':
    n = 4
    k = 2
    print(combine(n, k))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    n = 1
    k = 1
    print(combine(n, k))  # [[1]]
    n = 3
    k = 2
    print(combine(n, k))  # [[1, 2], [1, 3], [2, 3]]
    n = 5
    k = 0
    print(combine(n, k))  # [[]]
    n = 5
    k = 6
    print(combine(n, k))  # []
