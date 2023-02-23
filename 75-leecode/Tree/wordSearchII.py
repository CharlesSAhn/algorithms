'''

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

'''


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class TrieDS:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.isWord = True

    def search():
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.isWord


class Solution:
    def findWords(self, board, words):

        #Build Trie Tree
        tree = TrieDS()
        root = tree.root

        for word in words:
            tree.insert(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c, node, word ):

            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    board[r][c] not in node.children or (r,c) in visit ):

                return

            visit.add((r,c))
            node = node.children[board[r][c]]

            if node.isWord:
                res.add(word)

            dfs(r+1,c, node, word)
            dfs(r-1,c, node, word)
            dfs(r,c+1, node, word)
            dfs(r,c-1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")

        return list(res)



board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

s = Solution()
print(s.findWords(board, words))

