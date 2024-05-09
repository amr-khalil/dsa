"""
648. Replace Words
Solved
Medium
Topics
Companies
In English, we have a concept called root, which can be followed by some other word to form another longer word 
- let's call this word successor. For example, when the root "help" is followed by the successor word "ful", we can form a new word "helpful".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root,
replace it with the root that has the shortest length.
Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 
 
Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""

import collections


def replaceWords(dictionary, sentence):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    dictionary = set(dictionary)
    sentence = sentence.split()
    for i in range(len(sentence)):
        word = sentence[i]
        for j in range(1, len(word)):
            curr = sentence[i][:j]
            if curr in dictionary:
                sentence[i] = curr
                break
    return ' '.join(sentence)

# use trie
class TrieNode:
    def __init__(self):
        self.children =  collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        curr = ""
        for ch in word:
            if ch not in node.children:
                break
            node = node.children[ch]
            curr += ch
            if node.is_word:
                return curr
        return word


def replaceWords2(dictionary: list[str], sentence: str) -> str:
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
        
    ans = ""
    for word in sentence.split():
        if ans:
            ans += " "
        ans += trie.search(word)
    return ans

if __name__ == '__main__':
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replaceWords2(dictionary, sentence)) # the cat was rat by the bat
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(replaceWords2(dictionary, sentence)) # a a b c