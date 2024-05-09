
def vowels(string):
    """
    Count the number of vowels in a string
    vowels are a, e, i, o, u
    Example:
    vowels("hello") -> 2
    vowels("world") -> 1
    """
    count = 0
    for ch in string.lower():
        if ch in 'aeiou':
            count += 1
    print(count)
    
def vowels2(string):
    import re
    pattern = r'[aeiou]'
    ans = re.findall(pattern, string.lower())
    print(len(ans))

if __name__ == "__main__":
    vowels2("hello")
    vowels2("world")