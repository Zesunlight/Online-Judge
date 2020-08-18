import java.util.*;

/*
    90. 子集 II
    https://leetcode-cn.com/problems/subsets-ii/

    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    执行用时：2 ms, 在所有 Java 提交中击败了65.19%的用户
    内存消耗：40.2 MB, 在所有 Java 提交中击败了36.18%的用户
 */


class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        }

        for (int n : counter.keySet()) {
            List<List<Integer>> temp = new ArrayList<>();
            for (List<Integer> cand : subsets) {
                List<Integer> copy = new ArrayList<>(cand);
                for (int i = 0; i < counter.get(n); i++) {
                    copy.add(n);
                    List<Integer> increase = new ArrayList<>(copy);
                    temp.add(increase);
                }
            }
            subsets.addAll(temp);
        }
        return subsets;
    }
}


/*
public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> ans = new ArrayList<>();
    Arrays.sort(nums); //排序
    getAns(nums, 0, new ArrayList<>(), ans);
    return ans;
}

private void getAns(int[] nums, int start, ArrayList<Integer> temp, List<List<Integer>> ans) {
    ans.add(new ArrayList<>(temp));
    for (int i = start; i < nums.length; i++) {
        //和上个数字相等就跳过
        if (i > start && nums[i] == nums[i - 1]) {
            continue;
        }
        temp.add(nums[i]);
        getAns(nums, i + 1, temp, ans);
        temp.remove(temp.size() - 1);
    }
}

作者：windliang
链接：https://leetcode-cn.com/problems/subsets-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-19/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/


/*
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = [[]]
        cur = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                cur = [tmp + [nums[i]] for tmp in cur]
            else:
                cur = [tmp + [nums[i]] for tmp in res]
            res += cur
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-suan-fa-by-powcai-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/