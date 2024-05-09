"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest 
substring without repeating characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    Time complexity: O(n)
    Space complexity: O(min(m, n)), where n is the length of the string and m is the size of the character set.
    """
    ans = 0
    l = 0
    char_map = {}
    for r in range(len(s)):
        if s[r] in char_map:
            l = max(l, char_map[s[r]] + 1)
        char_map[s[r]] = r
        length = r - l + 1
        ans = max(ans, length)
    return ans

if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))  # 3
    s = "bbbbb"
    print(lengthOfLongestSubstring(s))  # 1
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))  # 3
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))  # 3
    s = " "
    print(lengthOfLongestSubstring(s))  # 1
    s = "au"
    print(lengthOfLongestSubstring(s))  # 2
    s = "aab"
    print(lengthOfLongestSubstring(s))  # 2
    s = "dvdf"
    print(lengthOfLongestSubstring(s))  # 3