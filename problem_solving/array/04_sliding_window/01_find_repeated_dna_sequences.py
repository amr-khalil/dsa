"""
187. Repeated DNA Sequences
Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the "10-letter-long"
sequences (substrings) that occur more than once in a DNA molecule. You may 
return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""

def findRepeatedDnaSequences(s):
    """
    return all the "10-letter-long" sequences (substrings) that occur more than once in a DNA molecule
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = set()
    # To store the repeated sequences
    repeated = set()
    # Iterate through the string. -9 because we need to find 10 letter long sequences
    for l in range(len(s)-9):
        substring = s[l:l+10]
        # If the substring is already in seen, add it to repeated
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    return list(repeated)

if __name__ == '__main__':
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # Output ["AAAAACCCCC","CCCCCAAAAA"]
    print(findRepeatedDnaSequences("AAAAAAAAAAAAA")) # Output ["AAAAAAAAAA"]    