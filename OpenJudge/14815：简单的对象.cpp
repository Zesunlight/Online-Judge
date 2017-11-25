#include <iostream>
using namespace std;

class A
{
	static int num;
public:
	A(){num+=1;}
	void func()
	{
		cout<< num <<endl;
	}
// 在此处补充你的代码
    A(const A & a) {

    }

    void func() const
	{
		cout<< num - 1 <<endl;
		--num;
	}
};

int A::num=1;
int main() {

    A a1;
	const A a2 = a1;
	A & a3 = a1;
	const A & a4 = a1;

	a1.func();
	a2.func();
	a3.func();
	a4.func();


	return 0;
}

/****************************************************
    Problem: 009:编程填空：简单的对象
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/009/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
