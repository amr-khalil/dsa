"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '(/)[]{}'.
"""


def valid_parentheses(string) -> bool:
    stack = []
    
    for ch in string:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == '(' and ch == ')':
                stack.pop()
            elif stack[-1] == '[' and ch == ']':
                stack.pop()
            elif stack[-1] == '{' and ch == '}':
                stack.pop()
            else:
                stack.append(ch)
    
    if stack:
        return False
    return True                
        
    
    
if __name__ == "__main__":
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("(]") == False
    
    print("PASSED")