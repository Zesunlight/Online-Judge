#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

void dfs(int a, int b);
int visited[12][12];
int n, m, x, y, record, times;
int main()
{

    int T;
    cin >> T;
    while(T--) {
        cin >> n >> m >> x >> y;
        memset(visited, 0, sizeof(visited));
        record = 0;
        times = 0;
        dfs(y, x);  //注意行列，x对应n，y对应m
        cout << times << endl;
    }

    return 0;
}

void dfs(int a, int b)
{
    visited[a][b] = 1;
    record++;
    if (a + 1 <= m - 1 && b - 2 >= 0) {
        if (visited[a + 1][b - 2] == 0) {
            dfs(a + 1, b - 2);
            record--;
            visited[a + 1][b - 2] = 0;
        }
    }
    if (a + 2 <= m - 1 && b - 1 >= 0) {
        if (visited[a + 2][b - 1] == 0) {
            dfs(a + 2, b - 1);
            record--;
            visited[a + 2][b - 1] = 0;
        }
    }
    if (a + 1 <= m - 1 && b + 2 <= n - 1) {
        if (visited[a + 1][b + 2] == 0) {
            dfs(a + 1, b + 2);
            record--;
            visited[a + 1][b + 2] = 0;
        }
    }
    if (a + 2 <= m - 1 && b + 1 <= n - 1) {
        if (visited[a + 2][b + 1] == 0) {
            dfs(a + 2, b + 1);
            record--;
            visited[a + 2][b + 1] = 0;
        }
    }

    if (a - 1 >= 0 && b - 2 >= 0) {
        if (visited[a - 1][b - 2] == 0) {
            dfs(a - 1, b - 2);
            record--;
            visited[a - 1][b - 2] = 0;
        }
    }
    if (a - 2 >= 0 && b - 1 >= 0) {
        if (visited[a - 2][b - 1] == 0) {
            dfs(a - 2, b - 1);
            record--;
            visited[a - 2][b - 1] = 0;
        }
    }
    if (a - 1 >= 0 && b + 2 <= n - 1) {
        if (visited[a - 1][b + 2] == 0) {
            dfs(a - 1, b + 2);
            record--;
            visited[a - 1][b + 2] = 0;
        }
    }
    if (a - 2 >= 0 && b + 1 <= n - 1) {
        if (visited[a - 2][b + 1] == 0) {
            dfs(a - 2, b + 1);
            record--;
            visited[a - 2][b + 1] = 0;
        }
    }

    if (record == n * m)
        times++;
}

/****************************************************
    Problem: 8465：马走日
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerfinal/002/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 38 ms
    Memory: 128 kB
    Date: 2017.09.24
*****************************************************/
