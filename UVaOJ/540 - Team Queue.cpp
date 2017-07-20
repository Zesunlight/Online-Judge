#include <cstdio>
#include <cstdlib>
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

int main()
{

    int teams = 0, scenario = 0;
    while (scanf("%d", &teams) != EOF && teams != 0) {
        printf("Scenario #%d\n", ++scenario);

        //队员编号和队伍编号的对应
        map<int, int> person;
        for (int i = 0; i < teams; i++) {
            int amount = 0;
            scanf("%d", &amount);
            while (amount--) {
                int temp = 0;
                scanf("%d", &temp);
                person[temp] = i;
            }
        }

        //整体的队伍的队列alphabet和各个队伍自己的队列subsidiary
        queue<int> alphabet, subsidiary[1007];
        char order[10] = "\0";
        while (scanf("%s", order) != EOF) {
            if (order[0] == 'S')
                break;
            else if (order[0] == 'E') {
                int enter = 0;
                scanf("%d", &enter);
                int team = person[enter];   //enter属于team这个队
                if (subsidiary[team].empty())   //enter是来排队的第一个人
                    alphabet.push(team);
                subsidiary[team].push(enter);
            } else if (order[0] == 'D') {
                int team = alphabet.front();
                printf("%d\n", subsidiary[team].front());
                subsidiary[team].pop();
                if (subsidiary[team].empty())   //team里最后一个人走了
                    alphabet.pop();
            }
        }

        printf("\n");   //next scenario
    }


    return 0;
}
