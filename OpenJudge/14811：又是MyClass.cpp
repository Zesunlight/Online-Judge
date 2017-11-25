#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;

// 在此处补充你的代码
template <class T>
class CMyClass {
public:
    T* arr;
    CMyClass(T start[], int leng) {
        arr = start;
    }
    T operator[] (int n) {
        return *(arr + n);
    }
};


int a[40];
int main() {

	int t;
	scanf("%d",&t);
	while ( t -- ) {
		int m;
		scanf("%d",&m);
		for (int i = 0;i < m; ++i)
			scanf("%d",a+i);
		char s[100];
		scanf("%s",s);
		CMyClass<int> b(a, m);
		CMyClass<char> c(s, strlen(s));
		printf("%d %c\n", b[5], c[7]);
	}

	return 0;
}

/****************************************************
    Problem: 005:编程填空：又是MyClass
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/005/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
