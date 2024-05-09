
def isAlienSorted(words, order):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    order = {ch: i for i, ch in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order[word1[j]] > order[word2[j]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True

if __name__ == '__main__':
    print(isAlienSorted(["hello", "like"], "hlabcdefgijkmnopqrstuvwxyz")) # True
    print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")) # False
    print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")) # False