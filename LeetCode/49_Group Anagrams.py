"""
    Problem: 49. Group Anagrams
    Website: https://leetcode.com/problems/group-anagrams/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 112 ms, faster than 79.25% of Python3 online submissions for Group Anagrams.
    Memory Usage: 16.8 MB, less than 41.51% of Python3 online submissions for Group Anagrams.
"""


class Solution:
    """
    Given an array of strings, group anagrams together.

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    """

    def groupAnagrams(self, strs):
        import collections
        organization = collections.defaultdict(list)

        for item in strs:
            organization[''.join(sorted(item))].append(item)

        return [group for group in organization.values()]


s = Solution()
a = []
print(s.groupAnagrams(a))


"""
单词字母出现的个数一致，判断为一个组。
26个元素的tuple作为key，记录每个字母出现的个数
"""