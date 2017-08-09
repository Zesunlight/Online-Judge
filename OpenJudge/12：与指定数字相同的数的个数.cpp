#include <iostream>
#include <set>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{

    int n = 0, temp = 0;
    multiset<int> number;
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &temp);
        number.insert(temp);
    }
    scanf("%d", &temp);
    printf("%d", number.count(temp));

    return 0;
}

/****************************************************
    Problem: 12
    Website: http://noi.openjudge.cn/ch0105/12/
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 0 ms
    Memory: 200 kB
*****************************************************/
