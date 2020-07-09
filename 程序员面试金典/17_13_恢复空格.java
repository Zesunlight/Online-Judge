import java.util.*;

/*
    面试题 17.13. 恢复空格
    https://leetcode-cn.com/problems/re-space-lcci/

    哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
    像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
    在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
    假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

    执行用时：800 ms, 在所有 Java 提交中击败了42.15%的用户
    内存消耗：40.9 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {
    public int respace(String[] dictionary, String sentence) {
        HashSet<String> set = new HashSet<>(Arrays.asList(dictionary));
        int len = sentence.length();
        int[] former = new int[len + 1];
        for (int end = 1; end < len + 1; ++end) {
            former[end] = former[end - 1] + 1;
            for (int start = 0; start < end; ++ start) {
                if (set.contains(sentence.substring(start, end))) {
                    former[end] = Math.min(former[end], former[start]);
                    if (former[end] == 0) break;
                }
            }
        }
        return former[len];
    }
    // https://leetcode-cn.com/problems/re-space-lcci/solution/cong-bao-li-ru-shou-you-hua-yi-ji-triezi-dian-shu-/
    // https://leetcode-cn.com/problems/re-space-lcci/solution/jian-dan-dp-trieshu-bi-xu-miao-dong-by-sweetiee/
}


// Trie字典树
class Solution_2 {
    /** 自定义一个TrieNode类型。
    * 这里不用建一个变量来存当前节点表示的字符，
    * 因为只要该节点不为null，就说明存在这个字符
    */
    class TrieNode{
        TrieNode[] childs;
        boolean isWord;
        public TrieNode(){
            childs = new TrieNode[26];
            isWord = false;
        }
    }
    TrieNode root;  //空白的根节点，设为全局变量更醒目
    public int respace(String[] dictionary, String sentence){
        root = new TrieNode();
        makeTrie(dictionary);   //创建字典树
        int n = sentence.length();
        int[] dp = new int[n+1];
        //这里从sentence最后一个字符开始
        for(int i=n-1; i>=0; i--){
            dp[i] = n-i;    //初始默认后面全不匹配
            TrieNode node = root;
            for(int j=i; j<n; j++){
                int c = sentence.charAt(j)-'a';               
                if(node.childs[c] == null){
                    //例如"abcde",i=1,j=2 可找出长度关系
                    dp[i] = Math.min(dp[i], j-i+1+dp[j+1]);
                    break;
                }
                if(node.childs[c].isWord){
                    dp[i] = Math.min(dp[i], dp[j+1]);
                } else{
                    dp[i] = Math.min(dp[i], j-i+1+dp[j+1]);
                }
                node = node.childs[c];
            }
        }
        return dp[0];
    }

    public void makeTrie(String[] dictionary){
        for(String str: dictionary){
            TrieNode node = root;
            for(int k=0; k<str.length(); k++){
                int i = str.charAt(k)-'a';
                if(node.childs[i] == null){
                    node.childs[i] = new TrieNode();
                }
                node = node.childs[i];
            }
            node.isWord = true; //单词的结尾
        }
    }
}

// 作者：tian-ye
// 链接：https://leetcode-cn.com/problems/re-space-lcci/solution/cong-bao-li-ru-shou-you-hua-yi-ji-triezi-dian-shu-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
