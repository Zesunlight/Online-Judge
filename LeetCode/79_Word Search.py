"""
    Problem: 79. Word Search
    Website: https://leetcode.com/problems/word-search/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 280 ms, faster than 95.01% of Python3 online submissions for Word Search.
    Memory Usage: 15 MB, less than 21.28% of Python3 online submissions for Word Search.
"""


class Solution:
    """
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    """

    def exist(self, board, word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ' '
                    if self.snake(board, word, 1, [i, j]):
                        return True
                    else:
                        board[i][j] = word[0]
        return False

    def snake(self, board, word, number, position):
        if number >= len(word):
            return True

        x, y = position
        left = board[x][y - 1] if y - 1 >= 0 else None
        right = board[x][y + 1] if y + 1 < len(board[x]) else None
        up = board[x - 1][y] if x - 1 >= 0 else None
        down = board[x + 1][y] if x + 1 < len(board) else None

        res = False
        if word[number] == left:
            board[x][y - 1] = ' '
            res += self.snake(board, word, number + 1, [x, y - 1])
            board[x][y - 1] = word[number]
            if res:
                return True
        if word[number] == right:
            board[x][y + 1] = ' '
            res += self.snake(board, word, number + 1, [x, y + 1])
            board[x][y + 1] = word[number]
            if res:
                return True
        if word[number] == up:
            board[x - 1][y] = ' '
            res += self.snake(board, word, number + 1, [x - 1, y])
            board[x - 1][y] = word[number]
            if res:
                return True
        if word[number] == down:
            board[x + 1][y] = ' '
            res += self.snake(board, word, number + 1, [x + 1, y])
            board[x + 1][y] = word[number]
            if res:
                return True

        return True if res else False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'SEE'
# word = 'ABCB'
print(s.exist(board, word))


"""
https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
"""