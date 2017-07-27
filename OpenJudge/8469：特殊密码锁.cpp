#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;
bool needTurn(string& s1, string& s2, int n);

int main()
{

    string initial, finally;
    cin >> initial >> finally;
    int time1 = 0, time2 = 0;
    int len = initial.length();

    string s1 = initial, s2 = finally;
    for (int i = 1; i < len-1; i++) {
        if (needTurn(s1, s2, i))
            time1++;
    }
    bool judge1 = (s1[len - 2] != s2[len - 2]) && (s1[len - 1] != s2[len - 1]);
    bool judge2 = (s1[len - 2] == s2[len - 2]) && (s1[len - 1] == s2[len - 1]);
    if (judge1 || judge2) {
        if (judge1)
            time1++;
    } else
        time1 = -1;

    if (initial[0] == '1')
        initial[0] = '0';
    else
        initial[0] = '1';
    if (initial[1] == '1')
        initial[1] = '0';
    else
        initial[1] = '1';
    time2++;
    for (int i = 1; i < len-1; i++) {
        if (needTurn(initial, finally, i))
            time2++;
    }
    judge1 = (initial[len - 2] != finally[len - 2]) && (initial[len - 1] != finally[len - 1]);
    judge2 = (initial[len - 2] == finally[len - 2]) && (initial[len - 1] == finally[len - 1]);
    if (judge1 || judge2) {
        if (judge1)
            time2++;
    } else
        time2 = -1;

    if ((time1 == -1) && (time2 == -1))
        cout << "impossible";
    else {
        if (time1 >= 0 && time2 >= 0)
            cout << min(time1, time2);
        else
            cout << time1 + time2 + 1;
    }

    return 0;
}

bool needTurn(string& s1, string& s2, int n)
{
    if (s1[n - 1] != s2[n - 1]) {
        s1[n - 1] = s2[n - 1];

        if (s1[n] == '0')
            s1[n] = '1';
        else
            s1[n] = '0';

        if (s1[n + 1] == '0')
            s1[n + 1] = '1';
        else
            s1[n + 1] = '0';

        return true;
    } else
        return false;
}
