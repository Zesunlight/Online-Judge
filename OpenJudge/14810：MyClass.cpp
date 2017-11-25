#include <iostream>
using namespace std;

class CMyClassA {
	int val;
public:
	CMyClassA(int);
	void virtual print();
};
CMyClassA::CMyClassA(int arg) {
	val = arg;
	printf("A:%d\n", val);
}
void CMyClassA::print() {
	printf("%d\n", val);
	return;
}
// 在此处补充你的代码
class CMyClassB:public CMyClassA {
public:
    CMyClassB(int arg):CMyClassA(arg + 10) {
        printf("B:%d\n", arg);
    }
    void virtual print() {
        printf("%d\n", 5);
        return;
    }
};

int main() {

	CMyClassA a(3), *ptr;
	CMyClassB b(5);
	ptr = &a; ptr->print();
	a = b;
	a.print();
	ptr = &b; ptr->print();

	return 0;
}

/****************************************************
    Problem: 004:编程填空：MyClass
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/004/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
