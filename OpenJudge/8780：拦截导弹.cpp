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
    int missile[30] = {0};
    int n = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> missile[i];
    int intercept[30] = {0};
    intercept[n - 1] = 1;
    for (int i = n-2; i >= 0; i--) {
        int maximum = 0;
        for (int j = i+1; j < n; j++) {
            if (missile[i] >= missile[j])
                if (intercept[j] > maximum)
                    maximum = intercept[j];
        }
        intercept[i] = maximum + 1;
    }
    int temp = intercept[0];
    for (int i = 1; i < n; i++)
        if (intercept[i] > temp)
            temp = intercept[i];
    cout << temp;

    return 0;
}

/****************************************************
    Problem: 8780
    Website: http://noi.openjudge.cn/ch0206/8780/
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 160 kB
*****************************************************/
