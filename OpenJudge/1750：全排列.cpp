#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

void arrange(string s, string result);

int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

//    srand(time(NULL));
//    for (int i = 0; i < 10; i++)
//        cout << rand() << endl;

    string s;
    cin >> s;
    string result;
    arrange(s, result);

    return 0;
}

void arrange(string s, string result)
{
    if (s.size() == 1) {
        cout << result << s << endl;
        //result.clear();
    } else {
        for (int i = 0; i < s.size(); i++) {
            string ss = s;
            string res = result;
            arrange(ss.erase(i, 1), res.append(&s[i], 1));
        }
    }
}
