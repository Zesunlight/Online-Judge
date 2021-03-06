# https://leetcode-cn.com/problems/UlBDOe/

'''
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves，
字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。
每部分树叶数量可以不相等，但均需大于等于 1。
每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。
请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
'''


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0] * 3 for _ in range(n)]
        hero = leaves[:3]
        dp[2] = [self.distance(hero, 'rrr'),
                 min(self.distance(hero, 'ryy'), self.distance(hero, 'rry')),
                 self.distance(hero, 'ryr')]
        
        for i in range(3, n):
            if leaves[i] == 'y':
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
                dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + 1
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
                dp[i][2] = min(dp[i - 1][1], dp[i - 1][2])
        
        return dp[n-1][2]
    
    def distance(self, a, b):
        diff = 0
        for i, j in zip(a, b):
            if i != j:
                diff += 1
        return diff

'''
class Solution {
public:
    int minimumOperations(string leaves) {
        int r = (leaves[0] != 'r') + (leaves[1] != 'r');
        int ry = (leaves[0] != 'r') + (leaves[1] != 'y');
        int ryr = ry;
        for (int i = 2; i < leaves.size(); i++) {
            ryr = min(ryr, ry) + (leaves[i] != 'r');
            ry = min(r, ry) + (leaves[i] != 'y');
            r += (leaves[i] != 'r');
        }
        return ryr;
    }
};

https://leetcode-cn.com/problems/UlBDOe/comments/612477
'''