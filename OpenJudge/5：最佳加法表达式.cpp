#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;

int isBig(string a, string b);
string add(string a, string b);
int main()
{

//    string num1, num2, result;
//    while (cin >> num1 >> num2) {
//        cout << isBig(num1, num2) << endl;
//        add(num1, num2, result);
//        cout << result << endl;
//        cout << result.substr(1, 2) << endl;
//    }

    int m = 0;
    string number;
    while (cin >> m >> number) {
        string value[m + 1][number.length() + 1];
        //initialize, value[a][b] means a '+' and b digits
        value[0][0] = "0";
        for (int i = 1; i <= number.length(); i++) {
            value[0][i] = number.substr(0, i);
            if (i <= m)
                value[i][0] = "0";
            for (int j = i; j <= m; j++)
                value[j][i] = "-1";
        }

        for (int i = 2; i <= number.length(); i++)
            for (int j = 1; j <= min(m, i-1); j++) {
                //value[j][i] = min{value[j - 1][k] + number.substr(k, i-k)}
                //k from j to i-1
                string minimum = add(value[j - 1][j], number.substr(j, i - j));
                for (int k = j+1; k <= i-1; k++) {
                    string res = add(value[j - 1][k], number.substr(k, i - k));
                    if (isBig(res, minimum) < 0)
                        minimum = res;
                }
                value[j][i] = minimum;
            }

        cout << value[m][number.length()] << endl;
    }

    return 0;
}

string add(string a, string b)
{
    int minimum = 0, maximum = 0;
    string temp, sum;
    if (a.length() >= b.length()) {
        temp = "0" + a;
        maximum = a.length();
        minimum = b.length();
    } else {
        temp = "0" + b;
        minimum = a.length();
        maximum = b.length();
    }
    int carry = 0, digit = 0;
    for (int i = 1; i <= minimum; i++) {
        digit = a[a.length() - i] - '0' + b[b.length() - i] - '0' + carry;
        carry = digit / 10;
        digit = digit % 10;
        temp[temp.length() - i] = '0' + digit;
    }
    if (a.length() == maximum) {
        for (int i = minimum + 1; i <= maximum; i++) {
            digit = a[a.length() - i] - '0' + carry;
            carry = digit / 10;
            digit = digit % 10;
            temp[temp.length() - i] = '0' + digit;
        }
    } else {
        for (int i = minimum + 1; i <= maximum; i++) {
            digit = b[b.length() - i] - '0' + carry;
            carry = digit / 10;
            digit = digit % 10;
            temp[temp.length() - i] = '0' + digit;
        }
    }
    if (carry > 0) {
        temp[0] = carry + '0';
        sum = temp;
    } else
        sum = temp.substr(1, temp.length() - 1);

    return sum;
}

int isBig(string a, string b)
{
    int result = 0;
    if (a.length() > b.length())
        result = 1;
    else if (a.length() < b.length())
        result = -1;
    else {
        if (a > b)
            result = 1;
        else if (a < b)
            result = -1;
        else
            result = 0;
    }
    return result;
}

/****************************************************
    Problem: 5
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw5/5/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 25 ms
    Memory: 256 kB
    Date: 2017.08.10
*****************************************************/
