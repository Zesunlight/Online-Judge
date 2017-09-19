#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <queue>
using namespace std;

struct point {
    int x;
    int y;
    int method;
};
void showPath(int xx, int yy);

point parent[105][105];
int k = 0, able = 1;
point now;

int main()
{

    int visited[105][105];
    memset(visited, 0, sizeof(visited));
    int a, b, c;
    cin >> a >> b >> c;
    queue<point> operation;

    point init = {0, 0, 0};
    operation.push(init);

    while (1) {
        now = operation.front();
        operation.pop();
        visited[now.x][now.y] =  1;
        if (now.x == c || now.y == c)
            break;

        if (visited[a][now.y] == 0) {
            point temp = {a, now.y, 0};
            operation.push(temp);
            parent[a][now.y] = {now.x, now.y, 1};  //fill(1)
        }
        if (visited[now.x][b] == 0) {
            point temp = {now.x, b, 0};
            operation.push(temp);
            parent[now.x][b] = {now.x, now.y, 2};  //fill(2)
        }
        if (visited[0][now.y] == 0) {
            point temp = {0, now.y, 0};
            operation.push(temp);
            parent[0][now.y] = {now.x, now.y, 3};  //drop(1)
        }
        if (visited[now.x][0] == 0) {
            point temp = {now.x, 0, 0};
            operation.push(temp);
            parent[now.x][0] = {now.x, now.y, 4};  //drop(2)
        }
        if (now.x + now.y > b) {
            point temp = {now.x + now.y - b, b, 0};
            if (visited[temp.x][temp.y] == 0) {
                operation.push(temp);
                parent[temp.x][temp.y] = {now.x, now.y, 5};  //pour(1, 2)
            }
        } else {
            point temp = {0, now.x + now.y, 0};
            if (visited[temp.x][temp.y] == 0) {
                operation.push(temp);
                parent[temp.x][temp.y] = {now.x, now.y, 5};  //pour(1, 2)
            }
        }
        if (now.x + now.y > a) {
            point temp = {a, now.x + now.y - a, 0};
            if (visited[temp.x][temp.y] == 0) {
                operation.push(temp);
                parent[temp.x][temp.y] = {now.x, now.y, 6};  //pour(1, 2)
            }
        } else {
            point temp = {now.x + now.y, 0, 0};
            if (visited[temp.x][temp.y] == 0) {
                operation.push(temp);
                parent[temp.x][temp.y] = {now.x, now.y, 6};  //pour(1, 2)
            }
        }

        if (operation.size() == 0) {
            able = 0;
            break;
        }
    }

    if (able == 0)
        cout << "impossible";
    else {
        showPath(now.x, now.y);
    }

    return 0;
}

void showPath(int xx, int yy)
{
    point curr = parent[xx][yy];
    if (!(curr.x == 0 && curr.y == 0)) {
        k++;
        showPath(curr.x, curr.y);
    }

    if (curr.x == 0 && curr.y == 0)
        cout << k + 1 << endl;
    switch (curr.method) {
        case 1:
            cout << "FILL(1)" << endl;
            break;
        case 2:
            cout << "FILL(2)" << endl;
            break;
        case 3:
            cout << "DROP(1)" << endl;
            break;
        case 4:
            cout << "DROP(2)" << endl;
            break;
        case 5:
            cout << "POUR(1,2)" << endl;
            break;
        case 6:
            cout << "POUR(2,1)" << endl;
            break;
    }
}
/****************************************************
    Problem: 2:Pots
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw9/2/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 296 kB
    Date: 2017.09.17
*****************************************************/
