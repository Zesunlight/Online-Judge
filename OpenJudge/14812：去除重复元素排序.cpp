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

int main() {

	int t;
	int  a[100];
	cin >> t;
	while(t--) {
		for(int i = 0;i < 12; ++i)
			cin >> a[i];
        // 在此处补充你的代码
        sort(a, a + 12);
        cout << a[0] << ' ';
        for (int i = 1; i < 12; i++) {
            if (a[i] == a[i - 1])
                continue;
            cout << a[i] << ' ';
        }
        vector<int> b;
        int c[2];
        //没搞清楚下面的是什么意思，不用它也可以通过
        //可能是想通过copy()来实现功能
        std::copy(b.begin(), b.end(), c);
		cout << endl;
	}

	return 0;
}

/****************************************************
    Problem: 006:编程填空：去除重复元素排序
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/006/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
