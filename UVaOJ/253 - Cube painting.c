#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
char first[7] = "\0";
char second[7] = "\0";

int sequence_four()
{
    //两头固定后，中间的会有4种变化
    int count = 0;
    if (first[2] == second[2]) {
        if (first[3] == second[3] && first[4] == second[4] && first[5] == second[5])
            count++;
    }
    if (first[3] == second[2]) {
        if (first[5] == second[3] && first[2] == second[4] && first[4] == second[5])
            count++;
    }
    if (first[4] == second[2]) {
        if (first[2] == second[3] && first[5] == second[4] && first[3] == second[5])
            count++;
    }
    if (first[5] == second[2]) {
        if (first[4] == second[3] && first[3] == second[4] && first[2] == second[5])
            count++;
    }

    if (count == 0)
        return -1;
    return 0;
}

int main()
{
//    freopen("INPUT.txt", "r", stdin);
//    freopen("OUTPUT.txt", "w", stdout);

    char ch = '\0';
    while ((ch = getchar()) != EOF) {
        for (int i = 1; i <= 6; i++) {
            first[i] = ch;
            ch = getchar();
        }
        for (int i = 1; i <= 6; i++) {
            second[i] = ch;
            ch = getchar();
        }

//        for (int i = 1; i <= 6; i++) {
//            putchar(first[i]);
//        }
//        printf("\n");
//        for (int i = 1; i <= 6; i++) {
//            putchar(second[i]);
//        }

        int times = 6;
        //找出与初始态等价的状态，一一比较
        // 1 2 3 4 5 6
        if (first[1] == second[1] && first[6] == second[6]) {
            times += sequence_four();
        } else
            times--;

        // 6 2 4 3 5 1
        if (first[6] == second[1] && first[1] == second[6]) {
            ch = first[3];
            first[3] = first[4];
            first[4] = ch;
            times += sequence_four();
            //restore
            ch = first[3];
            first[3] = first[4];
            first[4] = ch;
        } else
            times--;

        // 3 2 6 1 5 4
        if (first[3] == second[1] && first[4] == second[6]) {
            char a = first[3], b = first[4];
            first[3] = first[6];
            first[4] = first[1];
            times += sequence_four();
            //restore
            first[3] = a;
            first[4] = b;
        } else
            times--;

        // 4 2 1 6 5 3
        if (first[4] == second[1] && first[3] == second[6]) {
            char a = first[3], b = first[4];
            first[3] = first[1];
            first[4] = first[6];
            times += sequence_four();

            first[3] = a;
            first[4] = b;
        } else
            times--;

        // 2 6 3 4 1 5
        if (first[2] == second[1] && first[5] == second[6]) {
            char a = first[2], b = first[5];
            first[2] = first[6];
            first[5] = first[1];
            times += sequence_four();
            first[2] = a;
            first[5] = b;
        } else
            times--;

        // 5 1 3 4 6 2
        if (first[5] == second[1] && first[2] == second[6]) {
            char a = first[2], b = first[5];
            first[2] = first[1];
            first[5] = first[6];
            times += sequence_four();
            first[2] = a;
            first[5] = b;
        } else
            times--;

        if (times == 0)
            printf("FALSE\n");
        else
            printf("TRUE\n");
    }


	return 0;
}
