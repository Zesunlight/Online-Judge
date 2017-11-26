#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <fstream>
using namespace std;

class Printer{
// 在此处补充你的代码
public:
    int bound;
    Printer(int x):bound(x) {}

    void operator () (int data) {
        if (data > this->bound)
            cout << data << ',';
    }
    void operator () (string str) {
        if (str.length() > bound)
            cout << str + ',';
    }
};

int main() {

    int t;
	cin >> t;
	while(t--) {
		int n,x;
		cin>>x>>n;

		vector<int> intVec;
		for(int i = 0;i < n; ++i) {
			int y;
			cin >> y;
			intVec.push_back(y);
		}
		for_each(intVec.begin(), intVec.end(), Printer(x));
		cout<<endl;

		vector<string> strVec;
		for(int i = 0;i < n; ++i) {
			string str;
			cin >> str;
			strVec.push_back(str);
		}
		for_each(strVec.begin(), strVec.end(), Printer(x));
		cout<<endl;
	}

	return 0;
}

/****************************************************
    Problem: 012:编程填空：Printer
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/012/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.26
*****************************************************/
