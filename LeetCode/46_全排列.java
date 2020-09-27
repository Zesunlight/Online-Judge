import java.util.*;

/*
    46. 全排列
    https://leetcode-cn.com/problems/permutations/

    给定一个 没有重复 数字的序列，返回其所有可能的全排列。

    执行用时：2 ms, 在所有 Java 提交中击败了82.18%的用户
    内存消耗：39.1 MB, 在所有 Java 提交中击败了58.72%的用户
 */


class Solution {
    List<List<Integer>> answer = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        boolean[] visit = new boolean[nums.length];
        permute(nums, visit, new ArrayList<>());
        return answer;
    }

    public void permute(int[] nums, boolean[] visit, List<Integer> element) {
        if (element.size() == nums.length) {
            answer.add(new ArrayList<>(element));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (!visit[i]) {
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


class Solution2 {

    public List<List<Integer>> permute(int[] nums) {
        boolean[] visit = new boolean[nums.length];
        return dfs(nums);
    }

    public List<List<Integer>> dfs(int[] nums) {
        int n = nums.length;
        List<List<Integer>> permutation = new ArrayList<>();
        if (n == 1) {
            List<Integer> temp = new ArrayList<>();
            temp.add(nums[0]);
            permutation.add(temp);
        } else if (n == 0) {
            permutation.add(new ArrayList<>());
        } else {
            for (int i = 0; i < n; i++) {
                int[] rest = new int[n - 1];
                int index = 0;
                for (int j = 0; j < n; j++) {
                    if (i != j) {
                        rest[index] = nums[j];
                        index++;
                    }
                }
                for (List<Integer> ele : dfs(rest)) {
                    ele.add(nums[i]);
                    permutation.add(new ArrayList<>(ele));
                }
            }
        }
        return permutation;
    }
}


class Solution3 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        List<Integer> output = new ArrayList<Integer>();
        for (int num : nums) {
            output.add(num);
        }

        int n = nums.length;
        backtrack(n, output, res, 0);
        return res;
    }

    public void backtrack(int n, List<Integer> output, List<List<Integer>> res, int first) {
        // 所有数都填完了
        if (first == n) {
            res.add(new ArrayList<Integer>(output));
        }
        for (int i = first; i < n; i++) {
            // 动态维护数组
            Collections.swap(output, first, i);
            // 继续递归填下一个数
            backtrack(n, output, res, first + 1);
            // 撤销操作
            Collections.swap(output, first, i);
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。