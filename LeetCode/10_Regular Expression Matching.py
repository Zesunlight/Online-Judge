class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 1:
            if len(s) == 1:
                if p[0] == s[0] or p[0] == '.':
                    return True
            else:
                return False
        elif len(p) == 0:
            if len(s) == 0:
                return True
            return False
        elif len(s) == 0:
            if len(p) % 2 == 0:
                for i in range(int(len(p) / 2)):
                    if p[2*i+1] != '*':
                        return False
                return True
            else:
                return False

        ans = [[0 for _ in range(len(s))] for _ in range(len(p))]
        if p[0] == s[0] or p[0] == '.':
            ans[0][0] = 1
        if p[0] == s[0] and p[1] == '*':
            ans[1][0] = 1
            for i in range(1, len(s)):
                if s[i] == s[0]:
                    ans[1][i] = 1
                else:
                    break
        elif p[0] == '.' and p[1] == '*':
            for i in range(len(s)):
                ans[1][i] = 1
        elif (len(s)>1) and (p[0] == s[0] or p[0] == '.') and (p[1] == s[1] or p[1] == '.'):
            ans[1][1] = 1

        for i in range(2, len(p)):
            for j in range(len(s)):
                if p[i] == s[j] or p[i] == '.':
                    if j == 0 and i%2 == 0:
                        for k in range(int(i/2)):
                            if p[i-2*k-1] == '*':
                                ans[i][j] = 1
                            else:
                                ans[i][j] = 0
                                break
                    elif j != 0:
                        ans[i][j] = ans[i-1][j-1]
                elif p[i] == '*':
                    if p[i-1] == '.' or p[i-1] == s[j]:
                        ans[i][j] = (ans[i-2][j] or ans[i-1][j] or ans[i][j-1])
                    else:
                        ans[i][j] = ans[i-2][j]
        print(ans)
        if ans[len(p)-1][len(s)-1] > 0:
            return True
        else:
            return False

a = Solution()
print(a.isMatch("", "b*"))

'''
Recursion:
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    (first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

Dynamic Programming:
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

Explanation:
https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
'''

'''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s1 = re.compile(p).findall(s)
        if s1 == []:
            return False;
        if s1[0] == s:
            return True;
        else:
            return False;
'''
