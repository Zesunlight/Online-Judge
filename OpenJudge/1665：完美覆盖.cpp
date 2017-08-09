#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;

long long cover(int n);
long long occupy[40];
int main()
{

    int n = 0;
    scanf("%d", &n);
    for (int i = 1; i < 40; i += 2)
        occupy[i] = 0;
    for (int i = 4; i < 40; i += 2)
        occupy[i] = -1;
    occupy[0] = 1;
    occupy[2] = 3;
    //occupy[4] = 11;
    while (n != -1) {
        printf("%lld\n", cover(n));
        scanf("%d", &n);
    }


    return 0;
}

long long cover(int n)
{
    // f[n]=3*f[n-2]+2*(f[n-4]+..+f[0])，f[n]=4*f[n-2]-f[n-4]
    if (occupy[n] == -1) {
        if (occupy[n - 2] == -1)
            occupy[n] += cover(n - 2) * 4;
        else
            occupy[n] += occupy[n - 2] * 4;

        if (occupy[n - 4] == -1)
            occupy[n] -= cover(n - 4);
        else
            occupy[n] -= occupy[n - 4];

        occupy[n] += 1;
    }

    return occupy[n];
}

/****************************************************
    Problem: 1665
    Website: http://noi.openjudge.cn/ch0405/1665/
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
*****************************************************/
