
import collections

def firstUniqChar(s: str) -> int:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    count = collections.Counter(s)
    print(count)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

if __name__ == '__main__':
    print(firstUniqChar("leetcode")) # 0
    print(firstUniqChar("loveleetcode")) # 2
    print(firstUniqChar("aabb")) # -1
    print(firstUniqChar("aabbc")) # 4