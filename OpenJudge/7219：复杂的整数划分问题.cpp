#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;
int cutk(int n, int k);
int cut1(int n, int m);
int cut2(int n, int m);

int main()
{

    int n = 1, k = 1;
    while (cin >> n >> k) {
        cout << cutk(n, k) << endl;
        cout << cut1(n, n) << endl;
        int m = (n % 2) ? n : n-1;
        cout << cut2(n, m) << endl;
    }


    return 0;
}

int cutk(int n, int k)
{
    int result = 0;
    if (k == 0 || n < k)
        result = 0;
    else if (n == k || k == 1)
        result = 1;
    else {
        result = cutk(n-1, k-1) + cutk(n-k, k);   //k个数里有1 + 没有1
    }

    return result;
}

//n为划分的整数，m为划分中可取的最大值（不一定要取m）
int cut1(int n, int m)
{
    int result = 0;
    if (n == 1 || n == m*(m+1)/2)
        result = 1;
    else if (n > m*(m+1)/2)
        result = 0;
    else if (m >= n)
        result = 1 + cut1(n, n-1);
    else {
        result = cut1(n, m-1) + cut1(n-m, m-1); //划分中不取m + 划分中取一个m
    }
    return result;
}

int cut2(int n, int m)
{
    int result = 0;
    if (n == 1 || m == 1)
        result = 1;
    else if (m >= n) {
        m = (n % 2) ? n : n-1;
        if (m == 1)
            result = 1;
        else
            result = 1 + cut2(n, m-2);
    } else {
        result = cut2(n, m-2) + cut2(n-m, m); //划分中不取m + 划分中取一个m
    }
    return result;
}
/*
http://blog.csdn.net/athenaer/article/details/8265234
*/
