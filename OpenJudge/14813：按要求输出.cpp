#include <iostream>
#include <string>
#include <iterator>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stack>
using namespace std;

int  a[10] = {0, 6, 7, 3, 9, 5, 8, 6, 4, 9};
int  b[10] = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19};
int main() {

    // 在此处补充你的代码
    map<int, int> c;
    map<int, int>::iterator it;

	for(int i=0; i<10; i++)
		c[a[i]] = b[i];
	for(it=c.begin(); it!=c.end(); it++)
		cout<<it->second<<" ";

	return 0;
}

/****************************************************
    Problem: 007:编程填空：按要求输出
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/007/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
