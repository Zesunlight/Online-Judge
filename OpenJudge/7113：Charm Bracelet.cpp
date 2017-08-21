#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{

    int N = 0, M = 0;
    scanf("%d %d", &N, &M);
    int weight[N], desirability[N];
    int value[N][M + 1];
    //value[i][j]意为在前i个(从0开始数)bracelet中，承重为j的情况下的最大sum
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &weight[i], &desirability[i]);
        if (weight[i] > M)
            desirability[i] = 0;
    }

    for (int i = 0; i <= min(weight[0], M); i++)
        value[0][i] = 0;
    for (int i = weight[0]; i <= M; i++)
        value[0][i] = desirability[0];

    for (int i = 1; i < N; i++) {
        for (int j = 0; j <= M; j++) {
            if (j - weight[i] >= 0)
                value[i][j] = max(value[i - 1][j - weight[i]] + desirability[i], value[i - 1][j]);
            else
                value[i][j] = value[i - 1][j];
        }
    }

    printf("%d\n", value[N - 1][M]);

    return 0;
}

/****************************************************
    Problem: 7113-Charm Bracelet
    Website: http://noi.openjudge.cn/ch0206/7113/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 504 ms
    Memory: 65536 kB
    Date: 2017.08.19
*****************************************************/
