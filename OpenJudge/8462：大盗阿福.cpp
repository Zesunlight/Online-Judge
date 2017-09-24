#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int cash[100005];
int amount[100005];
int main()
{

    int T;
    cin >> T;
    while(T--) {
        int N;
        cin >> N;
        for (int i = 1; i <= N; i++)
            cin >> cash[i];
        memset(amount, 0, sizeof(amount));
        amount[1] = cash[1];
        amount[2] = max(cash[1], cash[2]);
        for (int i = 3; i <= N; i++) {
            amount[i] = max(amount[i-2] + cash[i], amount[i-1]);
        }
        cout << amount[N] << endl;
    }

    return 0;
}

/****************************************************
    Problem: 8462：大盗阿福
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerfinal/001/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 202 ms
    Memory: 4352 kB
    Date: 2017.09.23
*****************************************************/
