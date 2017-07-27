#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void index(int n);
int binary(int n, int number[20]);

int main()
{

//    srand(time(NULL));
//    for (int i = 0; i < 10; i++)
//        cout << rand() << endl;

    int n = 1;
    cin >> n;
//    int s[20];
//    int len = binary(n, s);
//    for (int i = len - 1; i >= 0; i--)
//        cout << s[i];
    index(n);

    return 0;
}

void index(int n)
{
    int number[20] = {0};
    int len = binary(n, number);
    if (n == 2) {
        cout << 2;
        return ;
    } else if (n == 1) {
        cout << "2(0)";
        return ;
    } else if (n == 3) {
        cout << "2+2(0)";
        return ;
    } else if (n == 0)
        return ;

    for (int i = len - 1; i >= 2; i--) {
        if (number[i] == 1) {
            cout << "2(";
            index(i);
            cout << ')';

            for (int j = i - 1; j >= 0; j--)
                if (number[j] == 1) {
                    cout << '+';
                    break;
                }
        }
    }
    index(number[0] + number[1] * 2);
}

int binary(int n, int number[20])
{
    int i = 0;
    for (; n > 0; i++) {
        number[i] = n & 1;
        n = n >> 1;
    }
    return i;
}
