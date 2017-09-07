#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int n, k, visited[10];
char board[10][10];
int dfs(int i, int j);
int main()
{

    while (cin >> n >> k) {
        if (n == -1 && k == -1)
            break;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> board[i][j];
        memset(visited, 0, sizeof(visited));
        cout << dfs(0, k) << endl;
    }

    return 0;
}

int dfs(int row, int rest)
{
    //start from row, there are rest chesses need to be located
    if (rest == 0)
        return 1;
    else if (rest > n - row)
        return 0;

    int number = 0;
    for (int i = 0; i < n; i++) {
        if (board[row][i] == '#' && visited[i] == 0) {
            visited[i] = 1;
            number += dfs(row + 1, rest - 1);
            visited[i] = 0;
        }
    }
    number += dfs(row + 1, rest);
    return number;
}

/****************************************************
    Problem: 3：棋盘问题
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw7/3/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 2 ms
    Memory: 136 kB
    Date: 2017.09.03
*****************************************************/
