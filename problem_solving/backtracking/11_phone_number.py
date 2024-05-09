"""
17. Letter Combinations of a Phone Number

Medium
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
def letterCombinations(digits):
    """
    Time complexity: O(4^n) 
    Space complexity: O(4^n)
    because each digit has 3 or 4 possible characters
    """
    def backtrack(index, path):
        # condition
        if len(digits) == len(path):
            ans.append(''.join(path))
            return
        # for selection in selections
        for i in range(index, len(digits)):
            # select
            key = digits[i]
            for ch in digits_map[key]:
                path.append(ch)
                # explore
                backtrack(index=i+1, path=path)
                # deselect
                path.pop()

    ans = []
    if not digits:
        return []
    backtrack(index=0, path=[])
    return ans


def letterCombinations2(digits):
        """
        Time complexity: O(4^n) 
        Space complexity: O(4^n)
        because each digit has 3 or 4 possible characters
        """

        if not digits:
            return []

        ans = ['']        
        for key in digits:
            curr = []
            for a in ans:
                for ch in digits_map[key]:
                    curr.append(a + ch)
            ans = curr
        return ans
    

if __name__ == '__main__':
    digits = "23"
    print(letterCombinations(digits))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    digits = ""
    print(letterCombinations(digits))  # []
    digits = "2"
    print(letterCombinations(digits))  # ["a","b","c"]
    digits = "234"
    print(letterCombinations(digits))  # ['adg', 'bdg', 'cdg', 'aeg', 'beg', 'ceg', 'afg', 'bfg', 'cfg', 'adh', 'bdh', 'cdh', 'aeh', 'beh', 'ceh', 'afh', 'bfh', 'cfh', 'adi', 'bdi', 'cdi', 'aei', 'bei', 'cei', 'afi', 'bfi', 'cfi']
