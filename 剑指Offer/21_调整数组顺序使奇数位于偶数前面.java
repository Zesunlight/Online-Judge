import java.util.*;

/*
    21. 调整数组顺序使奇数位于偶数前面
    https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分

    执行用时：2 ms, 在所有 Java 提交中击败了99.80%的用户
    内存消耗：47.9 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {

    public int[] exchange(int[] nums) {
        if (nums.length <= 1) return nums;
        int left = 0, right = nums.length - 1;
        while (true) {
            while (left < nums.length && nums[left] % 2 == 1) left++;
            while (right >= 0 && nums[right] % 2 == 0) right--;
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            } else break;
        }
        return nums;
    }

}


/*
    定义快慢双指针 fast 和 low ，fast 在前， low 在后 .
    fast 的作用是向前搜索奇数位置，low 的作用是指向下一个奇数应当存放的位置
    fast 向前移动，当它搜索到奇数时，将它和 nums[low] 交换，此时 low 向前移动一个位置 .
    重复上述操作，直到 fast 指向数组末尾 

class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int low = 0, fast = 0;
        while (fast < nums.size()) {
            if (nums[fast] & 1) {
                swap(nums[low], nums[fast]);
                low ++;
            }
            fast ++;
        }
        return nums;
    }
};

作者：huwt
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/ti-jie-shou-wei-shuang-zhi-zhen-kuai-man-shuang-zh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        p = 0
        for i, e in enumerate(nums):
            if e & 1:
                nums[i] = nums[p]
                nums[p] = e
                p += 1
        return nums

https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/comments/491945
*/


/*
return sorted(nums,key=lambda x:1-x%2)

https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/diao-zheng-qi-ou-shun-xu-pythontiao-jian-pai-xu-by/
*/
