#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int design(int ener, int num);
int main()
{

    int T, energy, number;
    cin >> T;
    while(T--) {
        cin >> energy >> number;
        cout << design(energy, number) << endl;
    }

    return 0;
}

int design(int ener, int num)
{
    int result = 0;
    if (num == 1 || ener == 0)
        result = 1;
    else {
        result += design(ener, num - 1);    //至少有一个影分身为0
        if (ener >= num)
            result += design(ener - num, num);  //没有影分身为0
    }
    return result;
}

/****************************************************
    Problem: 8467：鸣人的影分身
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerfinal/003/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 128 kB
    Date: 2017.09.24
*****************************************************/
