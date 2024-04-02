"""
Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses substring.


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


def longest_valid_parentheses(s) -> int:
    stack = []
    dp = [0] * (len(s) + 1)
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)
        

        
        
if __name__ == "__main__":
    string = "(()"
    print(longest_valid_parentheses(string))
    string = ")()())"
    print(longest_valid_parentheses(string))
    
