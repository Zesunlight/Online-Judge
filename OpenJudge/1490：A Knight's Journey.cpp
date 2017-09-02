#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int path[30][2];
int touched[30][30];
int number, p, q;
bool dfs(int i, int j);
int main()
{

    int n = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> p >> q;
        memset(touched, 0, sizeof(touched));
        cout << "Scenario #" << i << ':' << endl;
        int k = 1;
        for (; k <= q; k++) {
            int flag = 0;
            for (int m = 1; m <= p; m++) {
                number = 0;
                if (dfs(k, m)) {
                    flag = 1;
                    break;
                }
            }
            if (flag)
                break;
        }
        if (number < p*q)
            cout << "impossible\n\n";
        else {
            for (int j = 1; j <= number; j++)
                cout << (char)(path[j][0] + 'A' - 1) << path[j][1];
            cout << endl << endl;
        }
    }

    return 0;
}

bool dfs(int i, int j)
{
    number++;
    touched[i][j] = 1;
    path[number][0] = i;
    path[number][1] = j;
    if (i-2 > 0 && j-1 > 0 && touched[i-2][j-1] == 0)
        dfs(i - 2, j - 1);
    if (i-2 > 0 && j+1 <= p && touched[i-2][j+1] == 0)
        dfs(i - 2, j + 1);
    if (i-1 > 0 && j-2 > 0 && touched[i-1][j-2] == 0)
        dfs(i - 1, j - 2);
    if (i-1 > 0 && j+2 <= p && touched[i-1][j+2] == 0)
        dfs(i - 1, j + 2);
    if (i+1 <= q && j-2 > 0 && touched[i+1][j-2] == 0)
        dfs(i + 1, j - 2);
    if (i+1 <= q && j+2 <= p && touched[i+1][j+2] == 0)
        dfs(i + 1, j + 2);
    if (i+2 <= q && j-1 > 0 && touched[i+2][j-1] == 0)
        dfs(i + 2, j - 1);
    if (i+2 <= q && j+1 <= p && touched[i+2][j+1] == 0)
        dfs(i + 2, j + 1);

    if (number == p*q)
        return true;
    else {
        touched[i][j] = 0;
        number--;
        return false;
    }
}

/****************************************************
    Problem: 1490-A Knight's Journey
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw7/2/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 5 ms
    Memory: 136 kB
    Date: 2017.09.02 21:42:42
*****************************************************/
