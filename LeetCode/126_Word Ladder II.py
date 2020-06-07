"""
    Problem: 126. Word Ladder II
    Website: https://leetcode.com/problems/word-ladder-ii/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: 
    Runtime: 
    Memory Usage: 
"""


class Solution:
    """
    Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    """

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer/322524

        if endWord not in wordList:
            return []

        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                for i in range(len(word)): # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []


"""
https://leetcode.com/problems/word-ladder-ii/discuss/40475/My-concise-JAVA-solution-based-on-BFS-and-DFS

1). Use BFS to find the shortest distance between start and end, tracing the distance of crossing nodes from start node to end node, and store node's next level neighbors to HashMap;

2). Use DFS to output paths with the same distance as the shortest distance from distance HashMap: compare if the distance of the next level node equals the distance of the current node + 1.
"""