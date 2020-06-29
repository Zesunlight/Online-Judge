import java.util.*;

/*
    面试题 39. 数组中出现次数超过一半的数字
    https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

    执行用时：15 ms, 在所有 Java 提交中击败了24.73%的用户
    内存消耗：45 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


class Solution {
    public int majorityElement(int[] nums) {
        int len = nums.length;
        int common = len / 2;
        if (len == 1) {
            return nums[0];
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n: nums) {
            if (map.containsKey(n)) {
                int temp = map.get(n) + 1;
                if (temp > common) {
                    return n;
                }
                map.put(n, temp);
            } else {
                map.put(n, 1);
            }
        }
        return 0;
    }

    public int majorityElement_2(int[] nums) {
        int x = 0, votes = 0;
        for(int num : nums){
            if(votes == 0) x = num;
            votes += num == x ? 1 : -1;
        }
        return x;

//        作者：jyd
//        链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
//        来源：力扣（LeetCode）
//        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println();
    }
}