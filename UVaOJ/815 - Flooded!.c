#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int level[1000];

int cmp(const void* a, const void* b) {
    return *(int *)a - *(int *)b;
}

int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

    int m = 0, n = 0, region = 0;
    while ((scanf("%d%d", &m, &n)) != EOF) {
        if (m == 0 && n== 0)
            break;
        int total = m * n;
        region++;
        memset(level, 0, sizeof(level));
        for (int i = 0; i < total; i++)
            scanf("%d", &level[i]);
        int collect = 0;
        scanf("%d", &collect);

        int (*cmparator)(const void*, const void*) = cmp;
        qsort(level, total, sizeof(level[0]), cmparator);
//        for (int i = 0; i < m; i++) {
//            for (int j = 0; j < n; j++)
//                printf("%d ", level[m * i + j]);
//            printf("\n");
//        }

        int cover_regions = 0;
//        if (total == 1) {
//            printf("Region %d\n", region);
//            printf("Water level is %.2f meters.\n",(double)level[0] + collect / 100.0);
//            printf("100.00 percent of the region is under water.\n");
//        }

//挨个判断，淹一个柱子到与下一个柱子齐平的地方，看看用了多少水，总量里减去它
        while (collect > 0) {
            int increase = (level[cover_regions + 1] - level[cover_regions]) * 100 * (cover_regions + 1);
            if (increase > collect || cover_regions == total - 1) {
                //淹没不了下一个高楼了
                //可能是雨水不够了，或者是楼全淹没了
                printf("Region %d\n", region);
                double elevation = (double)level[cover_regions] + collect / 100.0 / (cover_regions + 1.0);
                printf("Water level is %.2f meters.\n", elevation);
                if (collect == 0)   //刚好和一栋楼持平，没有被淹
                    cover_regions--;
                double percent = (cover_regions + 1.0) * 100.0 / total;
                printf("%.2f percent of the region is under water.\n\n", percent);
                collect = 0;
            } else {
                cover_regions++;
                collect -= increase;
            }
        }
    }

	return 0;
}

/*
还可以这样想
假设所以的水填到一个柱子上，看看高度是不是比下一个柱子高
是的话，假设水只填这两个柱子，最后的高度怎么算呢
（水的总量/100 + 第一个柱子的高度 + 第二个柱子的高度） / 2
就是取平均
这样算简单很多
*/
