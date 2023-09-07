class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.endOfWord = True

    def pruneWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])

        visited = set()
        res = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, node, word):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
                node.endOfWord = False
                root.pruneWord(word)
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
