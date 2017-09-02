#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{

    int depth = 0, ball = 1, number = 0;
    scanf("%d", &number);
    while (number--) {
        scanf("%d%d", &depth, &ball);
        int total = (1 << depth) - 1, item = 1;
        while (item <= total) {
            if (ball % 2 == 0) {
                item = 2 * item + 1;
                ball /= 2;
            } else {
                item = 2 * item;
                ball = (ball + 1) / 2;
            }
        }
        printf("%d\n", item / 2);
    }
    scanf("%d", &number);

    return 0;
}

/****************************************************
    Problem: 679 - Dropping Balls
    Website: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=838&problem=620&mosmsg=Submission+received+with+ID+19891327
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 40 ms
    Memory:  kB
    Date: 2017.08.21
*****************************************************/
