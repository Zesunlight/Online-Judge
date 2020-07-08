import java.util.*;

/*
    面试题 16.11. 跳水板
    https://leetcode-cn.com/problems/diving-board-lcci/

    你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
    你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

    执行用时：1 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：47.7 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {
    public int[] divingBoard(int shorter, int longer, int k) {
        if (k == 0) return new int[0];
        if (shorter == longer) return new int[] {shorter * k};
        int[] res = new int[k + 1];
        int base = shorter * k;
        int step = longer - shorter;
        for (int i = 1; i < k + 1; ++i) {
            res[i] = base + step * i;
        }
        return res;
    }
}


/*
def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
    if k == 0: return []
    if longer == shorter: return [k*longer]
    return list(range(shorter*k, longer*k+1, (longer-shorter)))
*/