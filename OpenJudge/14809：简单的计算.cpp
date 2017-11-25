#include <iostream>
#include <string>
using namespace std;

template <class T>
class Add{
public:
// 在此处补充你的代码
    T a;
    Add(T n):a(n) {}
    T operator () (T x, T y) {
        return x + y - a;
    }
};

int main() {
	double f;
	int n;
	while( cin >> f >> n) {

		Add<double> a1(f);
		Add<int> a2(n);
		double x,y;
		int p,q;
		cin >> x >> y >> p >> q;
		cout << a1(x, y) << endl;
		cout << a2(p, q) << endl;
	}
	return 0;
}

/****************************************************
    Problem: 003:编程填空：简单的计算
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/003/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
