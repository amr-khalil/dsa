"""
409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

def longestPalindrome(s: str) -> int:
    odd_count = 0
    dic = {}
    # create a dictionary to store the frequency of each character
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
        # if the frequency of a character is odd, increment the odd_count
        if dic[ch] % 2 == 1:
            odd_count += 1
        # if the frequency of a character is even, decrement the odd_count
        else:
            odd_count -= 1
            
    # if there are more than one odd frequency characters, return the length of the string minus the odd_count plus 1
    if odd_count > 1:
        return len(s) - odd_count + 1
    # if there is only one odd frequency character, return the length of the string
    return len(s)


if __name__ == '__main__':
    s = "abccccdd"
    print(longestPalindrome(s)) # 7
    s = "a"
    print(longestPalindrome(s)) # 1
    