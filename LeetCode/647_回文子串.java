import java.util.*;

/*
    647. 回文子串
    https://leetcode-cn.com/problems/palindromic-substrings/

    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

    执行用时：2521 ms, 在所有 Java 提交中击败了5.00%的用户
    内存消耗：45.3 MB, 在所有 Java 提交中击败了5.04%的用户
 */


class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        if (n <= 1) return n;

        int[][] dp = new int[n][n];
        boolean[][] isPalindromic = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
            isPalindromic[i][i] = true;
        }
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = 3;
                isPalindromic[i][i + 1] = true;
            }
            else dp[i][i + 1] = 2;
        }

        for (int increase = 2; increase < n; increase++) {
            for (int i = 0; i < n - increase; i++) {
                int j = i + increase;
                dp[i][j] = 1 + dp[i][j - 1];
                if (s.charAt(j) == s.charAt(i) && isPalindromic[i + 1][j - 1]) isPalindromic[i][j] = true;
                for (int k = i; k < j; k++) {
                    if (s.charAt(j) == s.charAt(k) && (k + 1 > j - 1 || isPalindromic[k + 1][j - 1])) {
                        dp[i][j] += 1;
                    }
                }
            }
        }

        return dp[0][n - 1];
    }
}


class Solution2 {
    public int countSubstrings(String s) {
        int n = s.length(), ans = 0;
        for (int i = 0; i < 2 * n - 1; ++i) {
            int l = i / 2, r = i / 2 + i % 2;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                --l;
                ++r;
                ++ans;
            }
        }
        return ans;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


/*
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        ans = 0
        for d in range(n):
            for x in range(n):
                y = x + d
                if y >= n:
                    break
                if d == 0:
                    dp[x][y] = True
                elif d == 1:
                    dp[x][y] = (s[x] == s[y])
                else:
                    dp[x][y] = dp[x+1][y-1] and (s[x] == s[y])
                if dp[x][y]:
                    ans += 1
        return ans

https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/552164
*/


/*
const countSubstrings = (s) => {
  let count = 0;
  const len = s.length;

  const dp = new Array(len);
  for (let i = 0; i < len; i++) {
    dp[i] = new Array(len).fill(false);
  }

  for (let j = 0; j < len; j++) {
    for (let i = 0; i <= j; i++) {
      if (i == j) { // 单个字符
        dp[i][j] = true;
        count++;
      } else if (j - i == 1 && s[i] == s[j]) { // 两个相同的字符 
        dp[i][j] = true;
        count++;
      } else if (j - i > 1 && s[i] == s[j] && dp[i + 1][j - 1]) { // 多于两个字符
        dp[i][j] = true;
        count++;
      }
    }
  }
  return count;
};

作者：hyj8
链接：https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/