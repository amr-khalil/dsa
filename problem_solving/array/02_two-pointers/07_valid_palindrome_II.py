"""
680. Valid Palindrome II
Easy
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""


def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    if s == s[::-1]:
        return True
    
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            temp = s[:l] + s[l+1:] # remove left character
            temp2 = s[:r] + s[r+1:] # remove right character
            return temp == temp[::-1] or temp2 == temp2[::-1]
        
        l += 1
        r -= 1

if __name__ == "__main__":
    print(validPalindrome("aba"))  # True
    print(validPalindrome("abca"))  # True
    print(validPalindrome("abc"))  # False
    print(validPalindrome("dead"))  # True


