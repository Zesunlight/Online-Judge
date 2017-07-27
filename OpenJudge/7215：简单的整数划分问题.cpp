#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;
int cut(int n, int m);

int main()
{

    int n = 1;
    while (cin >> n)
        cout << cut(n, n) << endl;

    return 0;
}

//n为划分的整数，m为划分中可取的最大值（不一定要取m）
int cut(int n, int m)
{
    int result = 0;
    if (n == 1 || m == 1)
        result = 1;
    else if (m >= n)
        result = 1 + cut(n, n-1);
    else {
        result = cut(n, m-1) + cut(n-m, m); //划分中不取m + 划分中取一个m
    }
    return result;
}

/*
http://www.cnblogs.com/xubenben/p/3664959.html
http://www.cnblogs.com/hoodlum1980/archive/2008/10/11/1308493.html
*/
