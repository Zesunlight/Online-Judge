#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

string standard(string& s)
{
    string ans = s;
    for (unsigned i = 0; i < s.length(); i++)
        ans[i] = tolower(ans[i]);
    sort(ans.begin(), ans.end());
    return ans;
}

int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

    map<string, int> time;
    vector<string> words;
    string s;
    while (cin >> s) {
        if (s[0] == '#')
            break;
        words.push_back(s);
        string key = standard(s);
        if (time.count(key) == 0)
            time[key] = 1;
        else
            time[key]++;
    }

    vector<string> answer;
    for (unsigned i = 0; i < words.size(); i++) {
        if (time[standard(words[i])] == 1)
            answer.push_back(words[i]);
    }
    sort(answer.begin(), answer.end());
    for (unsigned i = 0; i < answer.size(); i++)
        cout << answer[i] << endl;

    return 0;
}
