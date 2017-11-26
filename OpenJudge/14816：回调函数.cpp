#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

class MyFunc
{
// 在此处补充你的代码
public:
    int power;
    MyFunc(int n):power(n) {}
    int operator() (int m) {
        int temp = 1;
        for (int i = 0; i < power; i++)
            temp *= m;
        return temp;
    }
};

int main() {

    int n;
	cin >> n;
	while(n--) {
		vector<MyFunc> v;
		for (int i = 0; i < 5; ++i)
			v.push_back(MyFunc(i+1));
		int ans = 1;
		for (int i = 0; i < 5; ++i)
		{
			int m;
			cin >> m;
			ans += v[i](m);
		}
		cout << ans <<endl;
	}


	return 0;
}

/****************************************************
    Problem: 010:编程填空：回调函数
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/010/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
