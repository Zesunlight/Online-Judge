#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

int invert(string a, string b);
int main()
{

    set<string> words;
    map<string, int> visited;
    string head, tail, get;
    cin >> head >> tail;
    words.insert(tail);
    visited[tail] = 0;
    while (cin >> get) {
        words.insert(get);
        visited[get] = 0;
    }
    queue<string> transfer;

    int success = 0;
    transfer.push(head);
    map<string, int> level;
    level[head] = 1;
    visited[head] = 1;
    while (!transfer.empty()) {
        string first = transfer.front();
        if (first == tail) {
            success = 1;
            break;
        }
        transfer.pop();

        for (set<string>::iterator j = words.begin(); j != words.end(); j++) {
            if (invert(first, *j) == 1 && visited[*j] == 0) {
                transfer.push(*j);
                visited[*j] = 1;
                level[*j] = level[first] + 1;
            }
        }
    }

    if (success == 1)
        cout << level[tail];
    else
        cout << '0';

    return 0;
}

int invert(string a, string b)
{
    int len = a.length();
    int diff = 0;
    for (int i = 0; i < len; i++) {
        if (a[i] != b[i])
            diff++;
    }
    return diff;
}

/****************************************************
    Problem: 8468：单词序列
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerfinal/006/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 152 kB
    Date: 2017.09.24
*****************************************************/
