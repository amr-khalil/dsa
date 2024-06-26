"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 

Constraints:
1 <= n <= 231 - 1
"""


def happy_number(n):
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def get_next(n):
        n = sum([int(i)**2 for i in str(n)])
        return n

    slow, fast = n, get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1


def happy_number2(n):
    seen = set()
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n in seen:
            return False
        seen.add(n)
    return True

if __name__ == "__main__":
    print(happy_number(19))  # True
    print(happy_number(2))  # False
    print(happy_number(7))  # True
    print(happy_number(1111111))  # True
    print(happy_number(11111111))  # False
