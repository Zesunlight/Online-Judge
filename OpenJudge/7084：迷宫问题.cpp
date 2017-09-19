#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <queue>
using namespace std;

struct point
{
    int x;
    int y;
};

void path(point father[7][7], int i, int j);
int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

    int maze[7][7], visited[7][7];
    point father[7][7];
    memset(maze, 1, sizeof(maze));
    memset(visited, 0, sizeof(visited));
    for (int i = 1; i < 6; i++)
        for (int j = 1; j < 6; j++)
            cin >> maze[i][j];

    queue<point> terminal;
    point temp = {1, 1};
    father[1][1] = {0, 0};
    terminal.push(temp);
    while (terminal.size() > 0) {
        temp = terminal.front();
        terminal.pop();
        int xx = temp.x, yy = temp.y;
        visited[xx][yy] = 1;
        if (xx == 5 && yy == 5)
            break;

        point temp1 = {xx - 1, yy};
        if (maze[xx - 1][yy] == 0 && visited[xx - 1][yy] == 0) {
            terminal.push(temp1);
            father[xx - 1][yy].x = xx;
            father[xx - 1][yy].y = yy;
        }

        point temp2 = {xx + 1, yy};
        if (maze[xx + 1][yy] == 0 && visited[xx + 1][yy] == 0) {
            terminal.push(temp2);
            father[xx + 1][yy].x = xx;
            father[xx + 1][yy].y = yy;
        }

        point temp3 = {xx, yy - 1};
        if (maze[xx][yy - 1] == 0 && visited[xx][yy - 1] == 0) {
            terminal.push(temp3);
            father[xx][yy - 1].x = xx;
            father[xx][yy - 1].y = yy;
        }

        point temp4 = {xx, yy + 1};
        if (maze[xx][yy + 1] == 0 && visited[xx][yy + 1] == 0) {
            terminal.push(temp4);
            father[xx][yy + 1].x = xx;
            father[xx][yy + 1].y = yy;
        }
    }

    //output path
    path(father, 5, 5);
    return 0;
}

void path(point father[7][7], int i, int j)
{
    if (i == 1 && j == 1)
        cout << "(0, 0)" << endl;
    else {
        path(father, father[i][j].x, father[i][j].y);
        cout << '(' << i - 1 << ", " << j - 1 << ')' << endl;
    }
}

/****************************************************
    Problem: 1:迷宫问题
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw9/1/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.09.10
*****************************************************/
