

def is_palindrome(string):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    l, r = 0, len(string) - 1
    
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("abba"))  # True
    print(is_palindrome("abcba"))  # True
    print(is_palindrome("abcde"))  # False
    print(is_palindrome("a"))  # True
    print(is_palindrome(""))  # True