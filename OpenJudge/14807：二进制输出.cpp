#include <iostream>
#include <string>
using namespace std;

string dec2bin(int x){
// 在此处补充你的代码
	string res = "0000000000000000000000000000000";
	for (int i = 30; i >= 0; i--) {
		int last = x & 1;
		res[i] = last + '0';
		x = x >> 1;
	}
	return res;
}
int main(){
	int n;
	cin >> n;
	while(n--) {
		int x;
		cin >> x;
		cout << dec2bin(x) << endl;
	}
	return 0;
}

/****************************************************
    Problem: 001:编程填空：二进制输出
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/001/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.25
*****************************************************/
