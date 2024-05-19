"""
205. Isomorphic Strings
Easy
Topics
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

def isIsomorphic(s: str, t: str) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    dic = {}
    for i in range(len(s)):
        key = s[i]
        val = t[i]
        if key in dic.keys():
            if dic[key] != val:
                return False
        else:
            if val in dic.values():
                return False
            dic[key] = val
    return True

if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t)) # True
    s = "foo"
    t = "bar"
    print(isIsomorphic(s, t)) # False
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t)) # True
    