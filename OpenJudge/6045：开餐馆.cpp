#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int place[110], salary[110];
int maximum[110];   //前i个地点可以获得的最大利润
int main()
{

    int T, n, k;
    cin >> T;
    while(T--) {
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> place[i];
        for (int i = 1; i <= n; i++)
            cin >> salary[i];

        maximum[1] = salary[1];
        for (int i = 2; i <= n; i++) {
            int temp = i - 1;
            while (temp > 0 && place[i] - place[temp] <= k)
                temp--;
            if (temp > 0)
                maximum[i] = max(maximum[i - 1], maximum[temp] + salary[i]);
            else
                maximum[i] = max(maximum[i - 1], salary[i]);
        }

        cout << maximum[n] << endl;
    }

    return 0;
}

/****************************************************
    Problem: 6045：开餐馆
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerfinal/004/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 40 ms
    Memory: 716 kB
    Date: 2017.09.24
*****************************************************/
