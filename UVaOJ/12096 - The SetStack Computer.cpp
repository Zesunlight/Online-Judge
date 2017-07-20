#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#define ALL(x) x.begin(), x.end()
using namespace std;

map<set<int>, int> set_to_id;
vector<set<int>> id_to_set;

int findID(set<int> s)
{
    if (set_to_id.count(s))
        return set_to_id[s];
    else
        id_to_set.push_back(s); //add s to vector
    set_to_id[s] = id_to_set.size() - 1;    //add s to map
    return set_to_id[s];
}

int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

    int number = 0;
    scanf("%d", &number);
    while (number--) {
        stack<int> sta;
        int operate = 0;
        scanf("%d", &operate);
        string str;
        for (int i = 0; i < operate; i++) {
            cin >> str;
            if (str == "PUSH")
                sta.push(findID(set<int>()));   //insert empty set
            else if (str == "DUP")
                sta.push(sta.top());
            else {
                set<int> set1 = id_to_set[sta.top()];
                sta.pop();
                set<int> set2 = id_to_set[sta.top()];
                sta.pop();
                set<int> set0;
                if (str == "UNION")
// iterator set_union( iterator start1, iterator end1, iterator start2, iterator end2, \
                        iterator result, StrictWeakOrdering cmp );
                    set_union(ALL(set1), ALL(set2), inserter(set0, set0.begin()));
                else if (str == "INTERSECT")
                    set_intersection(ALL(set1), ALL(set2), inserter(set0, set0.begin()));
                else if (str == "ADD") {
                    set0 = set2;
                    set0.insert(findID(set1));
                }
                sta.push(findID(set0));
            }
            cout << id_to_set[sta.top()].size() << endl;
        }
        cout << "***" << endl;
    }


    return 0;
}
