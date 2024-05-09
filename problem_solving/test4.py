"""

array = ['eye', 'california', '12321', 'Level', 'Was it a cat I saw'] 
output = 'Was it a cat I saw'

"""


def is_palindorme(s):
    s1 = s.replace(" ", "").lower()
    s2 = s1[::-1]
    return s1 == s2

def longest_palindrome(array):
    length = -1
    ans = ""
    for string in array:
        if is_palindorme(string):
            if len(string) > length:
                length = len(string)
                ans = string
    if length == -1:
        return -1
    return ans

if __name__ == '__main__':
    print(longest_palindrome(['eye', 'california', '12321', 'Level', 'Was it a cat I saw'])) # 'Was it a cat I saw'
    print(longest_palindrome(['Dubai', 'amman', 'cairo', 'fes'])) # 'Was it a cat I saw'
