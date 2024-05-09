"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
"""

def generateParenthesis(n):
    """
    Time complexity: O(4^n/sqrt(n))
    Space complexity: O(4^n/sqrt(n))
    result => 4^n/sqrt(n) combinations
    """
    def backtrack(path, l, r):
        # if meet the condition
        if len(path) == 2 * n:
            ans.append(path)
            return
        # for selection in selections
        if l < n:
            # select
            backtrack(path+'(', l+1, r)
        if r < l:
            # select
            backtrack(path+')', l, r+1)
            
    ans = []
    backtrack(path='', l=0, r=0)
    return ans

if __name__ == '__main__':
    n = 3
    print(generateParenthesis(n))  # ["((()))","(()())","(())()","()(())","()()()"]
    n = 1
    print(generateParenthesis(n))  # ["()"]
    n = 2
    print(generateParenthesis(n))  # ["(())","()()"]