/*
    551. 学生出勤记录 I
    https://leetcode-cn.com/problems/student-attendance-record-i/

    给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
    'A'：Absent，缺勤
    'L'：Late，迟到
    'P'：Present，到场
    如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
    按 总出勤 计，学生缺勤（'A'）严格 少于两天。
    学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。
    如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

    执行用时：0 ms
    内存消耗：36.4 MB
 */


class Solution {
    public boolean checkRecord(String s) {
        int absent = 0;
        int late = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'A':
                    absent++;
                    late = 0;
                    break;
                case 'L':
                    late++;
                    break;
                case 'P':
                    late = 0;
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + s.charAt(i));
            }
            if (absent >= 2) {
                return false;
            }
            if (late >= 3) {
                return false;
            }
        }
        return true;
    }
}
