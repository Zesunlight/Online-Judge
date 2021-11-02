import java.util.HashSet;
import java.util.Set;

/*
    575. 分糖果
    https://leetcode-cn.com/problems/distribute-candies/

    Alice 有 n 枚糖，其中第 i 枚糖的类型为 candyType[i] 。Alice 注意到她的体重正在增长，所以前去拜访了一位医生。
    医生建议 Alice 要少摄入糖分，只吃掉她所有糖的 n / 2 即可（n 是一个偶数）。Alice 非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。
    给你一个长度为 n 的整数数组 candyType ，返回： Alice 在仅吃掉 n / 2 枚糖的情况下，可以吃到糖的最多种类数。

    执行用时：25 ms
    内存消耗：40.5 MB
 */

class Solution {
    public int distributeCandies(int[] candyType) {
        int n = candyType.length;
        Set<Integer> set = new HashSet<>();
        int diff = 0;
        for (int i : candyType) {
            if (!set.contains(i)) {
                set.add(i);
                diff++;
            }
            if (diff == n / 2) {
                break;
            }
        }
        return diff;
    }
    
    public int distributeCandies2(int[] candyType) {
        // 链接：https://leetcode-cn.com/problems/distribute-candies/solution/fen-tang-guo-by-leetcode-solution-l4f6/
        Set<Integer> set = new HashSet<Integer>();
        for (int candy : candyType) {
            set.add(candy);
        }
        return Math.min(set.size(), candyType.length / 2);
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.distributeCandies(new int[] {1, 1, 1, 1}));
    }
}
