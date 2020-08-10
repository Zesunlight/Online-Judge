import java.util.*;

/*
    78. 子集
    https://leetcode-cn.com/problems/subsets/

    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    执行用时：2 ms, 在所有 Java 提交中击败了28.42%的用户
    内存消耗：39.8 MB, 在所有 Java 提交中击败了86.62%的用户
 */


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        if (nums.length == 0) {
            List<List<Integer>> temp = new ArrayList<>();
            temp.add(new ArrayList<>());
            return temp;
        }
        List<List<Integer>> result = subsets(Arrays.copyOfRange(nums, 0, nums.length - 1));
        List<List<Integer>> append = new ArrayList<>(result);
        for (List<Integer> l : append) {
            List<Integer> temp = new ArrayList<>(l);
            temp.add(nums[nums.length - 1]);
            result.add(temp);
        }
        return result;
    }
}


class Solution2 {
  public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> output = new ArrayList();
    output.add(new ArrayList<Integer>());

    for (int num : nums) {
      List<List<Integer>> newSubsets = new ArrayList();
      for (List<Integer> curr : output) {
        newSubsets.add(new ArrayList<Integer>(curr){{add(num);}});
      }
      for (List<Integer> curr : newSubsets) {
        output.add(curr);
      }
    }
    return output;
  }
}

// 作者：LeetCode
// 链接：https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> output = new ArrayList();
        int n = nums.length;

        for (int i = (int)Math.pow(2, n); i < (int)Math.pow(2, n + 1); ++i) {
            // generate bitmask, from 0..00 to 1..11
            String bitmask = Integer.toBinaryString(i).substring(1);

            // append subset corresponding to that bitmask
            List<Integer> curr = new ArrayList();
            for (int j = 0; j < n; ++j) {
                if (bitmask.charAt(j) == '1') curr.add(nums[j]);
            }
            output.add(curr);
        }
        return output;
    }
}

// 作者：LeetCode
// 链接：https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


/*
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  

作者：powcai
链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
