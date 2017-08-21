#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
    int w, h, m;
    while (scanf("%d%d%d", &w, &h, &m) != -1) {
        if (w == 0 && h == 0 && m == 0)
            break;
        int area[w + 1][h + 1][m + 1];
        //area[i][j][k]意为长为i宽为j切成k块时，最大面积的下限
        for (int i = 0; i <= w; i++) {
            for (int j = 0; j <= h; j++) {
                area[i][j][0] = 1000;
                area[i][j][1] = i * j;
            }
        }
        for (int i = 0; i <= w; i++)
            for (int k = 0; k <= m; k++)
                area[i][0][k] = 1000;
        for (int j = 0; j <= h; j++)
            for (int k = 0; k <= m; k++)
                area[0][j][k] = 1000;

        for (int i = 1; i <= w; i++) {
            for (int j = 1; j <= h; j++) {
                for (int k = 2; k <= m; k++) {
                    area[i][j][k] = 1000;
                    for (int p = 1; p <= i; p++) {
                        for (int q = 1; q <= k; q++) {
                            //所有的切成k块的方式中，选取最小值
                            if (max(area[p][j][q], area[i - p][j][k - q]) < area[i][j][k])
                                area[i][j][k] = max(area[p][j][q], area[i - p][j][k - q]);
                        }
                    }
                    for (int p = 1; p <= j; p++) {
                        for (int q = 1; q <= k; q++) {
                            if (max(area[i][p][q], area[i][j - p][k - q]) < area[i][j][k])
                                area[i][j][k] = max(area[i][p][q], area[i][j - p][k - q]);
                        }
                    }
                }
            }
        }
        printf("%d\n", area[w][h][m]);
    }

    return 0;
}

/****************************************************
    Problem: 6047-分蛋糕
    Website: http://noi.openjudge.cn/ch0405/6047/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 128 ms
    Memory: 103 kB
    Date: 2017.08.20
*****************************************************/
