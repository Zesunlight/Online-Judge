import java.util.*;

/*
    126. 单词接龙 II
    https://leetcode-cn.com/problems/word-ladder-ii/

    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。
    转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换后得到的单词必须是字典中的单词。

    执行用时:1190 ms, 在所有 Java 提交中击败了7.05%的用户
    内存消耗:42.8 MB, 在所所有 Java 提交中击败了79.27%的用户
 */


class Solution {
    int pathLength;
    List<List<String>> path = new ArrayList<>();
    HashMap<String, List<String>> transform = new HashMap<>();
    Set<String> visit = new HashSet<>();
    HashMap<String, Integer> layer = new HashMap<>();

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return new ArrayList<>();

        if (!wordList.contains(beginWord)) {
            List<String> temp = new ArrayList<>();
            for (String value : wordList) {
                if (arrive(value, beginWord)) {
                    temp.add(value);
                }
            }
            transform.put(beginWord, temp);
        }

        for (int i = 0; i < wordList.size(); ++i) {
            List<String> target = new ArrayList<>();
            for (int j = 0; j < wordList.size(); ++j) {
                if (i == j) continue;
                if (arrive(wordList.get(i), wordList.get(j))) {
                    target.add(wordList.get(j));
                }
            }
            transform.put(wordList.get(i), target);
        }

        layer.put(beginWord, 1);
        Queue<String> candidate = new LinkedList<>();
        candidate.offer(beginWord);
        visit.add(beginWord);
        bfs(candidate);

        visit.clear();
        visit.add(beginWord);
        pathLength = wordList.size() + 2;
        List<String> start = new ArrayList<>();
        start.add(beginWord);
        dfs(beginWord, endWord, start, 1);

        return path;
    }

    public void bfs(Queue<String> candidate) {
        int depth = 1;
        while (!candidate.isEmpty()) {
            depth++;
            int height = candidate.size();
            for (int i = 0; i < height; i++) {
                String start = candidate.poll();
                for (String next : transform.get(start)) {
                    if (!visit.contains(next)) {
                        visit.add(next);
                        layer.put(next, depth);
                        candidate.offer(next);
                    }
                }
            }
        }
    }

    public void dfs(String current, String endWord, List<String> curPath, int length) {
        if (layer.get(current) < length) return;
        if (length >= pathLength && !current.equals(endWord)) return;

        if (current.equals(endWord)) {
            if (length < pathLength) {
                pathLength = length;
                path.clear();
            }
            path.add(new ArrayList<>(curPath));
        } else {
            for (String next : transform.get(current)) {
                if (!visit.contains(next)) {
                    visit.add(next);
                    curPath.add(next);
                    dfs(next, endWord, curPath, length + 1);
                    visit.remove(next);
                    curPath.remove(length);
                }
            }
        }
    }

    public boolean arrive(String a, String b) {
        int difference = 0;
        for (int i = 0; i < a.length(); ++i) {
            if (a.charAt(i) != b.charAt(i)) ++difference;
            if (difference >= 2) return false;
        }
        return true;
    }

}


class Solution2 {
    private static final int INF = 1 << 20;
    private Map<String, Integer> wordId; // 单词到id的映射
    private ArrayList<String> idWord; // id到单词的映射
    private ArrayList<Integer>[] edges; // 图的边

    public Solution() {
        wordId = new HashMap<>();
        idWord = new ArrayList<>();
    }

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        int id = 0;
        // 将wordList所有单词加入wordId中 相同的只保留一个 // 并为每一个单词分配一个id
        for (String word : wordList) {
            if (!wordId.containsKey(word)) { 
                wordId.put(word, id++);
                idWord.add(word);
            }
        }
        // 若endWord不在wordList中 则无解
        if (!wordId.containsKey(endWord)) {
            return new ArrayList<>();
        }
        // 把beginWord也加入wordId中
        if (!wordId.containsKey(beginWord)) {
            wordId.put(beginWord, id++);
            idWord.add(beginWord);
        }

        // 初始化存边用的数组
        edges = new ArrayList[idWord.size()];
        for (int i = 0; i < idWord.size(); i++) {
            edges[i] = new ArrayList<>();
        }
        // 添加边
        for (int i = 0; i < idWord.size(); i++) {
            for (int j = i + 1; j < idWord.size(); j++) {
                // 若两者可以通过转换得到 则在它们间建一条无向边
                if (transformCheck(idWord.get(i), idWord.get(j))) {
                    edges[i].add(j);
                    edges[j].add(i);
                }
            }
        }

        int dest = wordId.get(endWord); // 目的ID
        List<List<String>> res = new ArrayList<>(); // 存答案
        int[] cost = new int[id]; // 到每个点的代价
        for (int i = 0; i < id; i++) {
            cost[i] = INF; // 每个点的代价初始化为无穷大
        }

        // 将起点加入队列 并将其cost设为0
        Queue<ArrayList<Integer>> q = new LinkedList<>();
        ArrayList<Integer> tmpBegin = new ArrayList<>();
        tmpBegin.add(wordId.get(beginWord));
        q.add(tmpBegin);
        cost[wordId.get(beginWord)] = 0;

        // 开始广度优先搜索
        while (!q.isEmpty()) {
            ArrayList<Integer> now = q.poll();
            int last = now.get(now.size() - 1); // 最近访问的点
            if (last == dest) { // 若该点为终点则将其存入答案res中
                ArrayList<String> tmp = new ArrayList<>();
                for (int index : now) {
                    tmp.add(idWord.get(index)); // 转换为对应的word
                }
                res.add(tmp);
            } else { // 该点不为终点 继续搜索
                for (int i = 0; i < edges[last].size(); i++) {
                    int to = edges[last].get(i);
                    // 此处<=目的在于把代价相同的不同路径全部保留下来
                    if (cost[last] + 1 <= cost[to]) {
                        cost[to] = cost[last] + 1;
                        // 把to加入路径中
                        ArrayList<Integer> tmp = new ArrayList<>(now); tmp.add(to);
                        q.add(tmp); // 把这个路径加入队列
                    }
                }
            }
        }
        return res;
    }

    // 两个字符串是否可以通过改变一个字母后相等
    boolean transformCheck(String str1, String str2) {
        int differences = 0;
        for (int i = 0; i < str1.length() && differences < 2; i++) {
            if (str1.charAt(i) != str2.charAt(i)) {
                ++differences;
            }
        }
        return differences == 1;
    } 
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/word-ladder-ii/solution/dan-ci-jie-long-ii-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
