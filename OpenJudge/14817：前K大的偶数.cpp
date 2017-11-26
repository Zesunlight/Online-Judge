#include <iostream>
#include <vector>
#include <set>
using namespace std;

class MyQueue
{
// 在此处补充你的代码
public:
    int even;
    multiset<int, greater<int> > data;
    MyQueue(int k):even(k) {}
    friend ostream& operator << (ostream& cout, MyQueue& q) {
        multiset<int, greater<int> >::iterator it;
        for (it = q.data.begin(); it != q.data.end(); ++it) {
            if (*it % 2 == 0) {
                cout << *it << ' ';
                --q.even;
            }
            if (q.even == 0) {
                break;
            }
        }
        return cout;
    }
    friend istream& operator >> (istream& cin, MyQueue& q) {
        int item = 0;
        cin >> item;
        q.data.insert(item);
        return cin;
    }
};

int main() {

    int t;
	cin >> t;
	while(t--) {
		int n, k;
		cin >> n >> k;
		MyQueue q(k);
		for (int i = 0; i < n; ++i)
			cin >> q;
		cout<<q;
		cout << endl;
	}

	return 0;
}

/****************************************************
    Problem: 011:编程填空：前K大的偶数
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/011/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 818 ms
    Memory: 18048 kB
    Date: 2017.11.26
*****************************************************/
