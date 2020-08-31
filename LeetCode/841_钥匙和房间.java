/*
    841. 钥匙和房间
    https://leetcode-cn.com/problems/keys-and-rooms/

    有 N 个房间，开始时你位于 0 号房间。
    每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
    在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 
    钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
    最初，除 0 号房间外的其余所有房间都被锁住。
    你可以自由地在房间之间来回走动。
    如果能进入每个房间返回 true，否则返回 false。

    执行用时：3 ms, 在所有 Java 提交中击败了39.43%的用户
    内存消耗：39.7 MB, 在所有 Java 提交中击败了65.12%的用户
 */


class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        Set<Integer> set = new HashSet<>();
        set.add(0);
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        while (!queue.isEmpty()) {
            List<Integer> keys = rooms.get(queue.poll());
            int visit = 0;
            for (Integer i : keys) {
                if (set.contains(i)) visit++;
                else {
                    set.add(i);
                    queue.offer(i);
                }
            }
        }
        return set.size() == n;
    }
}


class Solution2 {
    boolean[] vis;
    int num;

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        num = 0;
        vis = new boolean[n];
        dfs(rooms, 0);
        return num == n;
    }

    public void dfs(List<List<Integer>> rooms, int x) {
        vis[x] = true;
        num++;
        for (int it : rooms.get(x)) {
            if (!vis[it]) {
                dfs(rooms, it);
            }
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/keys-and-rooms/solution/yao-chi-he-fang-jian-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。