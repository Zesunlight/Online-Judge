#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int marble[10010] = {0};
int main()
{

    int number = 0, query = 0;
    int Case = 0, which = 0;
//    freopen("INPUT.txt", "r", stdin);
//    freopen("OUTPUT.txt", "w", stdout);

    while (scanf("%d%d", &number, &query) == 2) {
        if (number == 0 && query == 0)
            break;
        for (int i = 0; i < number; i++)
            scanf("%d", &marble[i]);
        sort(marble, marble + number);
//        for (int i = 0; i < number; i++)
//            printf("%d", marble[i]);

        printf("CASE# %d:\n", ++Case);
        while (query--) {
            scanf("%d", &which);
            int position = lower_bound(marble, marble + number, which) - marble;
            //lower_bound 返回的是指针
            //printf("position = %d\n", position);
            if (marble[position] == which)
                printf("%d found at %d\n", which, position + 1);
            else
                printf("%d not found\n", which);
        }
    }
    return 0;
}


/*STL中的实现
这个算法中，first是最终要返回的位置
int lower_bound(int *array, int size, int key)
{
    int first = 0, middle;
    int half, len;
    len = size;

    while(len > 0) {
        half = len >> 1;
        middle = first + half;
        if(array[middle] < key) {
            first = middle + 1;
            len = len-half-1;       //在右边子序列中查找
        }
        else
            len = half;            //在左边子序列（包含middle）中查找
    }
    return first;
}
*/
