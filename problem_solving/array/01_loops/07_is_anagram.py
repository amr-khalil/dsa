
def is_anagram(str1, str2):
    """
    anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase,
    typically using all the original letters exactly once.
    hello -> olleh = True
    hello -> world = False
    """
    
    str1 = "".join(sorted(list(str1)))
    str2 = "".join(sorted(list(str2)))
    return str1 == str2


if __name__ == "__main__":
    print(is_anagram("hello", "olleh"))
    print(is_anagram("hello", "world"))