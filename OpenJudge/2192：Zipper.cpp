#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{

    int n = 0;
    scanf("%d", &n);
    char s1[205], s2[205], s3[405];
    int match[205][205];
    for (int i = 1; i <= n; i++) {
        scanf("%s%s%s", s1, s2, s3);
        int len1 = strlen(s1);
        int len2 = strlen(s2);

        match[0][0] = 1;
        for (int j = 1; j <= len1; j++)
            if (s3[j - 1] == s1[j - 1] && match[j - 1][0] == 1)
                match[j][0] = 1;
            else
                match[j][0] = 0;
        for (int j = 1; j <= len1; j++)
            if (s3[j - 1] == s2[j - 1] && match[0][j - 1] == 1)
                match[0][j] = 1;
            else
                match[0][j] = 0;

        for (int j = 1; j <= len1; j++)
            for (int k = 1; k <= len2; k++) {
                if (s3[j + k - 1] == s1[j - 1] && match[j - 1][k] == 1)
                    match[j][k] = 1;
                else if (s3[j + k - 1] == s2[k - 1] && match[j][k - 1] == 1)
                    match[j][k] = 1;
                else
                    match[j][k] = 0;
            }

        if (match[len1][len2] == 1)
            printf("Data set %d: yes\n", i);
        else
            printf("Data set %d: no\n", i);
    }

    return 0;
}

/****************************************************
    Problem: 2192
    Website: http://bailian.openjudge.cn/practice/2192/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 17 ms
    Memory: 640 kB
    Date: 2017.08.09
*****************************************************/
