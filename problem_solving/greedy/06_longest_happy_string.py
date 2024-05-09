"""
1405. Longest Happy String
Medium
Topics
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 
Constraints:
0 <= a, b, c <= 100
a + b + c > 0
"""

import collections

def longestDiverseString(a: int, b: int, c: int) -> str:
    """
    """
    count = collections.Counter({'a':a, 'b':b, 'c':c})
    res = ['#']
    while True:
        (a1, _), (a2, _) = count.most_common(2)
        
        if a1 == res[-1] == res[-2]:
            a1 = a2
            
        if not count[a1]:
            break
            
        res.append(a1)
        count[a1] -= 1            
    
    return ''.join(res[1:])

if __name__ == '__main__':
    a = 1
    b = 1
    c = 7
    print(longestDiverseString(a, b, c)) # ccaccbcc
    a = 7
    b = 1
    c = 0
    print(longestDiverseString(a, b, c)) # aabaa
    a = 1
    b = 1
    c = 1
    print(longestDiverseString(a, b, c)) # abc
    a = 2
    b = 2
    c = 1
    print(longestDiverseString(a, b, c)) # ababac
    a = 7
    b = 1
    c = 1
    print(longestDiverseString(a, b, c)) # ababababac