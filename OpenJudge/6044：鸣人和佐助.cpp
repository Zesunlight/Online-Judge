#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int M, N, T;
int mkrf_i, mkrf_j, zovu_i, zovu_j;
int minTime, time_, cost;
char chase[205][205];
int length[205][205][12];
//length[i][j][k] 从起点走到(i, j)且花费k的情况下的最短长度，也是最短时间
void dfs(int x, int y);
int main()
{

    cin >> M >> N >> T;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> chase[i][j];
            if (chase[i][j] == '@') {
                mkrf_i = i;
                mkrf_j = j;
            }
//            if (chase[i][j] == '+') {
//                zovu_i = i;
//                zovu_j = j;
//            }
        }
    }

    minTime = 1 << 30;
    time_ = 0;
    cost = 0;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k <= T; k++)
                length[i][j][k] = minTime;
    for (int i = 0; i <= T; i++)
        length[mkrf_i][mkrf_j][i] = 0;

    dfs(mkrf_i, mkrf_j);
    if (minTime == 1 << 30)
        cout << "-1";
    else
        cout << minTime;

    return 0;
}

void dfs(int x, int y)
{
    //from (x, y) to zovu, the min time is dfs(x, y)
    if (cost > T)
        return;
    if (chase[x][y] == '+') {
        minTime = min(minTime, time_);
        return;
    }
    int attack = 0;
    if (x > 0) {
        attack = chase[x - 1][y] == '#' ? 1 : 0;
        if (time_ + 1 < length[x - 1][y][cost + attack]) {
            length[x - 1][y][cost + attack] = time_ + 1;
            time_++;
            cost += attack;
            dfs(x - 1, y);
            time_--;
            cost -= attack;
        }
    }
    if (x < M - 1) {
        attack = chase[x + 1][y] == '#' ? 1 : 0;
        if (time_ + 1 < length[x + 1][y][cost + attack]) {
            length[x + 1][y][cost + attack] = time_ + 1;
            time_++;
            cost += attack;
            dfs(x + 1, y);
            time_--;
            cost -= attack;
        }
    }
    if (y > 0) {
        attack = chase[x][y - 1] == '#' ? 1 : 0;
        if (time_ + 1 < length[x][y - 1][cost + attack]) {
            length[x][y - 1][cost + attack] = time_ + 1;
            time_++;
            cost += attack;
            dfs(x, y - 1);
            time_--;
            cost -= attack;
        }
    }
    if (y < N - 1) {
        attack = chase[x][y + 1] == '#' ? 1 : 0;
        if (time_ + 1 < length[x][y + 1][cost + attack]) {
            length[x][y + 1][cost + attack] = time_ + 1;
            time_++;
            cost += attack;
            dfs(x, y + 1);
            time_--;
            cost -= attack;
        }
    }
}

/****************************************************
    Problem: 6044-鸣人和佐助
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw8/1/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 199 ms
    Memory: 2092 kB
    Date: 2017.09.03
*****************************************************/
