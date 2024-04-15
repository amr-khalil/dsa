"""
79. Word Search
Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?


board =[['E', 'D', 'X', 'I', 'W'],
        ['P', 'U', 'F', 'M', 'Q'],
        ['I', 'C', 'A', 'T', 'E'],
        ['M', 'A', 'L', 'C', 'A'],
        ['J', 'T', 'I', 'V', 'E']]
         
word = "EDUCATIVE", r=5, c=5, index=9
r | c | index | board[r][c] | word[index] | status
------------------------------------------------------------------------
0 | 0 | 0     | E           | E           | Match, recurse with index+1
0 | 1 | 1     | D           | D           | Match, recurse with index+1
0 | 2 | 1     | X           | U           | No match, backtrack
1 | 1 | 2     | U           | U           | Match, recurse with index+1
1 | 2 | 2     | F           | C           | No match, backtrack
2 | 1 | 2     | C           | C           | Match, recurse with index+1
2 | 2 | 3     | A           | A           | Match, recurse with index+1
2 | 3 | 4     | T           | T           | Match, recurse with index+1
2 | 4 | 4     | E           | I           | No match, backtrack
3 | 3 | 4     | C           | I           | No match, backtrack
1 | 4 | 4     | M           | I           | No match, backtrack
3 | 2 | 4     | L           | T           | No match, backtrack 
1 | 2 | 4     | F           | T           | No match, backtrack  
3 | 1 | 5     | A           | A           | Match, recurse with index+1
3 | 2 | 5     | L           | T           | No match, backtrack
4 | 1 | 6     | T           | T           | Match, recurse with index+1
4 | 2 | 7     | I           | I           | Match, recurse with index+1
4 | 3 | 8     | V           | V           | Match, recurse with index+1
4 | 4 | 9     | E           | E           | Match, recurse with index+1
"""

def word_search(grid, word):
    if not grid:
        return False
    
    rows, cols = len(grid), len(grid[0])
    
    def backtrack(r, c, index):
        # Base case: All characters are found
        if index == len(word):
            return True

        # Requirements:
        # 1. Check if out of bounds
        if not (0 <= r < rows and 0 <= c < cols):
            return False  

        # 2. Check if character does not match
        if grid[r][c] != word[index]:
            return False  

        # 3. Check if cell has been visited
        if grid[r][c] == '#':
            return False

        # Mark
        # the cell as visited by changing its content temporarily
        temp = grid[r][c]
        grid[r][c] = '#'

        # Search
        # Neighbors (up, down, left, right)
        if (backtrack(r - 1, c, index + 1) or
            backtrack(r + 1, c, index + 1) or
            backtrack(r, c - 1, index + 1) or
            backtrack(r, c + 1, index + 1)):
            return True
        
        # Unmark
        # the cell by restoring its original value
        grid[r][c] = temp
        return False
    
    # Check each cell as a potential starting point
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):  # Start the search from each cell
                return True
    
    return False
    
    
if __name__ == '__main__':
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"
    print(word_search(board, word))  # True
    word = "ABCB"
    print(word_search(board, word))  # False
    
    board = [ ['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']]
    word = "warrior"
    print(word_search(board, word))  # True
    word = "hello"
    # print(word_search(board, word))  # False