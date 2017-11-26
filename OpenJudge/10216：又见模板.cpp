#include <iostream>
#include <algorithm>
#include <list>
#include <cstring>
#include <fstream>
using namespace std;

// 在此处补充你的代码
template <class T, int n>
class A {
public:
    T* a;
    A(T* b) {
        a = b;
    }
    T sum() {
        T temp;
        for (int i = 0; i < n; i++)
            temp = temp + a[i];
        return temp;
    }
    T operator [] (int c) {
        return a[c];
    }
};

int main() {

    int t;
	cin >> t;
	while( t -- ) {
	    int b1[10];
	    for(int i = 0;i < 10; ++i)

	    	cin >> b1[i];
	    A<int, 10> a1 = b1;
	    cout << a1[2] << endl;


	    double b2[5] ;
	    for(int i = 0;i < 5; ++i)
	    	cin >> b2[i];

	    A<double, 5> a2 = b2;
	    cout << a2.sum() << endl;


	    string b3[4] ;
	    for(int i = 0;i < 4; ++i)
	    	cin >> b3[i];

	    A<string, 4> a3 = b3;
	    cout << a3.sum() << endl;
	}

	return 0;
}

/****************************************************
    Problem: 014:编程填空：又见模板
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/014/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.26
*****************************************************/
