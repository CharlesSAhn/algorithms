'''

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

'''


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):

            current_node = root

            for i in range(j, len(word)):

                char = word[i]
                if char == ".":
                    for childNode in current_node.children.values():
                        if dfs(i + 1, childNode):
                            return True

                    return False
                else:
                    if char not in current_node.children:
                        return False
                    current_node = current_node.children[char]


            return current_node.word

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)