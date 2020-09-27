import java.util.*;

/*
    47. 全排列 II
    https://leetcode-cn.com/problems/permutations-ii/

    给定一个可包含重复数字的序列，返回所有不重复的全排列。

    执行用时：1 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：39.6 MB, 在所有 Java 提交中击败了47.89%的用户
 */


class Solution {
    List<List<Integer>> answer = new ArrayList<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        boolean[] visit = new boolean[nums.length];
        Arrays.sort(nums);
        permute(nums, visit, new ArrayList<>());
        return answer;
    }

    public void permute(int[] nums, boolean[] visit, List<Integer> element) {
        if (element.size() == nums.length) {
            answer.add(new ArrayList<>(element));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (!visit[i]) {
                    if (i > 0 && nums[i] == nums[i - 1] && !visit[i - 1]) continue;
                    visit[i] = true;
                    element.add(nums[i]);
                    permute(nums, visit, element);
                    element.remove(element.size() - 1);
                    visit[i] = false;
                }
            }
        }
    }
}