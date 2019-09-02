"""
    Problem: 72. Edit Distance
    Website: https://leetcode.com/problems/edit-distance/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 164 ms, faster than 81.60% of Python3 online submissions for Edit Distance.
    Memory Usage: 17.7 MB, less than 15.38% of Python3 online submissions for Edit Distance.
"""
from pprint import pprint


class Solution:
    """
    Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
    You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
    """

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)

        dp = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
        dp[0][0] = 0 if word1[0] == word2[0] else 1

        for i in range(1, len(word1)):
            dp[i][0] = i if word1[i] == word2[0] else dp[i - 1][0] + 1
        for j in range(1, len(word2)):
            dp[0][j] = j if word1[0] == word2[j] else dp[0][j - 1] + 1

        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # delete insert replace
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        pprint(dp)
        return dp[-1][-1]


s = Solution()
word1 = "intention"
word2 = "execution"
print(s.minDistance(word1, word2))


"""
https://leetcode.com/problems/edit-distance/discuss/25846/C++-O(n)-space-DP

To apply DP, we define the state dp[i][j] to be the minimum number of operations to convert word1[0..i) to word2[0..j).
For the base case, that is, to convert a string to an empty string, the mininum number of operations (deletions) is just the length of the string. 
So we have dp[i][0] = i and dp[0][j] = j.

For the general case to convert word1[0..i) to word2[0..j), we break this problem down into sub-problems. 
Suppose we have already known how to convert word1[0..i - 1) to word2[0..j - 1) (dp[i - 1][j - 1]), 
if word1[i - 1] == word2[j - 1], then no more operation is needed and dp[i][j] = dp[i - 1][j - 1].

If word1[i - 1] != word2[j - 1], we need to consider three cases.
Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1);
If word1[0..i - 1) = word2[0..j) then delete word1[i - 1] (dp[i][j] = dp[i - 1][j] + 1);
If word1[0..i) + word2[j - 1] = word2[0..j) then insert word2[j - 1] to word1[0..i) (dp[i][j] = dp[i][j - 1] + 1).
So when word1[i - 1] != word2[j - 1], dp[i][j] will just be the minimum of the above three cases.
"""

"""
https://web.stanford.edu/class/cs124/lec/med.pdf
"""