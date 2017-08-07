#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

char str[100005];
int label[100005];
int main()
{

    while (scanf("%s", str+1) != -1) {    //start from s[1]
        int n = strlen(str+1);
        int current = 0, last = 0;
        label[0] = -1;
        for (int i = 1; i <= n; i++) {
            if (str[i] == '[') {
                //last = current;   //actually last already equal to current
                current = 0;
            } else if (str[i] == ']') {
                current = last;     //that is last's funcation
            } else {
                label[i] = label[current];  //add a new node
                label[current] = i;
                if (last == current)
                    last = i;
                current = i;
            }
        }

        for (int i = label[0]; i != -1; i = label[i])
            printf("%c", str[i]);
        printf("\n");
    }



    return 0;
}

/****************************************************
    Problem: 11988
    Website: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=838&problem=3139&mosmsg=Submission+received+with+ID+19816397
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 20 ms
    Memory: 0 kb
*****************************************************/
