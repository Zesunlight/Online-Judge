import java.util.*;

/*
    93. 复原IP地址
    https://leetcode-cn.com/problems/restore-ip-addresses/

    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

    执行用时:7 ms, 在所有 Java 提交中击败了30.19%的用户
    内存消耗:40 MB, 在所所有 Java 提交中击败了32.99%的用户
 */


class Solution {
    public List<String> restoreIpAddresses(String s) {
        return restoreIpAddresses(s, 4);
    }

    public List<String> restoreIpAddresses(String s, int n) {
        List<String> res = new ArrayList<>();
        if (s.length() < n || s.length() > 3 * n) return res;
        if (n == 1) {
            if (s.length() >= 2 && s.charAt(0) == '0') return res;
            if (s.length() == 3 && Integer.parseInt(s) > 255) return res;
            res.add(s);
            return res;
        }

        for (String str : restoreIpAddresses(s.substring(1), n - 1)) {
            String possible = s.substring(0, 1) + '.' + str;
            res.add(possible);
        }

        if (s.charAt(0) == '0' || s.length() < 2) return res;
        for (String str : restoreIpAddresses(s.substring(2), n - 1)) {
            String possible = s.substring(0, 2) + '.' + str;
            res.add(possible);
        }

        if (s.charAt(0) == '0' || s.length() < 3) return res;
        if (Integer.parseInt(s.substring(0, 3)) <= 255) {
            for (String str : restoreIpAddresses(s.substring(3), n - 1)) {
                String possible = s.substring(0, 3) + '.' + str;
                res.add(possible);
            }
        }
        return res;
    }

}


class Solution2 {
    static final int SEG_COUNT = 4;
    List<String> ans = new ArrayList<String>();
    int[] segments = new int[SEG_COUNT];

    public List<String> restoreIpAddresses(String s) {
        segments = new int[SEG_COUNT];
        dfs(s, 0, 0);
        return ans;
    }

    public void dfs(String s, int segId, int segStart) {
        // 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
        if (segId == SEG_COUNT) {
            if (segStart == s.length()) {
                StringBuffer ipAddr = new StringBuffer();
                for (int i = 0; i < SEG_COUNT; ++i) {
                    ipAddr.append(segments[i]);
                    if (i != SEG_COUNT - 1) {
                        ipAddr.append('.');
                    }
                }
                ans.add(ipAddr.toString());
            }
            return;
        }

        // 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
        if (segStart == s.length()) {
            return;
        }

        // 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
        if (s.charAt(segStart) == '0') {
            segments[segId] = 0;
            dfs(s, segId + 1, segStart + 1);
        }

        // 一般情况，枚举每一种可能性并递归
        int addr = 0;
        for (int segEnd = segStart; segEnd < s.length(); ++segEnd) {
            addr = addr * 10 + (s.charAt(segEnd) - '0');
            if (addr > 0 && addr <= 0xFF) {
                segments[segId] = addr;
                dfs(s, segId + 1, segEnd + 1);
            } else {
                break;
            }
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/fu-yuan-ipdi-zhi-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
