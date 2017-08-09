#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{

    vector<int> tree;
    int height = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &height);
        tree.push_back(height);
    }
    scanf("%d", &height);
    height += 30;
    sort(tree.begin(), tree.end());
    int time = 0;
    vector<int>::iterator it = tree.begin();
    for (; it != tree.end(); it++)
        if (*it <= height)
            time++;
    printf("%d", time);

    return 0;
}

/****************************************************
    Problem: 2
    Website: http://noi.openjudge.cn/ch0106/02/
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 200 kB
*****************************************************/
