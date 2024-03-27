from functools import reduce


def is_palindrom1(string):
    return string == reduce(lambda x,y : y+x, string)

def is_palindrom2(string):
    return all([string[i] == string[~i]
                for i in range(len(string)//2)])

if __name__ == "__main__":
    string = "abba"
    print(is_palindrom2(string))
    