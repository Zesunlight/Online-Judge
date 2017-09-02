#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

int touched[21][21];
char brick[21][21];
int number, W, H;
void dfs(int i, int j);
int main()
{

    cin >> W >> H;
    while (W != 0 && H != 0) {
        memset(touched, 0, sizeof(touched));
        number = 0;
        int start_i = 0, start_j = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cin >> brick[i][j];
                if (brick[i][j] == '@') {
                    start_i = i;
                    start_j = j;
                }
            }
        }
        dfs(start_i, start_j);
        cout << number << endl;

        cin >> W >> H;
    }

    return 0;
}

void dfs(int i, int j)
{
    number++;
    touched[i][j] = 1;
    if (i > 0 && brick[i-1][j] == '.' && touched[i-1][j] == 0)
        dfs(i - 1, j);
    if (j > 0 && brick[i][j-1] == '.' && touched[i][j-1] == 0)
        dfs(i, j - 1);
    if (i < H-1 && brick[i+1][j] == '.' && touched[i+1][j] == 0)
        dfs(i + 1, j);
    if (j < W-1 && brick[i][j+1] == '.' && touched[i][j+1] == 0)
        dfs(i, j + 1);
}

/****************************************************
    Problem: 1818-红与黑
    Website: http://cxsjsxmooc.openjudge.cn/2017t2summerw7/1/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 4 ms
    Memory: 184 kB
    Date: 2017.09.02
*****************************************************/
