/*
    202. 快乐数
    https://leetcode-cn.com/problems/happy-number/

    编写一个算法来判断一个数 n 是不是快乐数。
    「快乐数」定义为：
    对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
    然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
    如果 可以变为  1，那么这个数就是快乐数。
    如果 n 是快乐数就返回 true ；不是，则返回 false 。

    执行用时：1 ms
    内存消耗：35.3 MB
 */

class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = nextNum(n);

        while (fast != 1 && slow != fast) {
            slow = nextNum(slow);
            fast = nextNum(nextNum(fast));
        }

        return fast == 1;
    }

    public int nextNum(int n) {
        int res = 0;
        while (n > 0) {
            int m = n % 10;
            n = n / 10;
            res += m*m;
        }
        return res;
    }
    
    private int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            totalSum += d * d;
        }
        return totalSum;
    }

    public boolean isHappy2(int n) {
        // 链接：https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
        Set<Integer> seen = new HashSet<>();
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            n = getNext(n);
        }
        return n == 1;
    }

}
