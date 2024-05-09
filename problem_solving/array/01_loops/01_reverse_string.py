
from functools import reduce

def reverse_string1(string):
    return string[::-1]

def reverse_string2(string):
    ans = ""
    for ch in string:
        ans = ch + ans 
    return ans

def reverse_string3(string):
    ans = reduce(lambda rev, ch: ch + rev, string)
    return ans
        
if __name__ == "__main__":
    string = "12345 67890"
    print(reverse_string1(string))
    