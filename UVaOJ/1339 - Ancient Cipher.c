#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void* a, const void* b) {
    return *(int *)a - *(int *)b;
}
int main()
{
	char origin[110] = "\0";
	char change[110] = "\0";
	int ori[30] = {0};
	int cha[30] = {0};
	int flag = 1;
//	for (int i = 0; i < 26; i++)
//        printf("%d %d\n", ori[i], cha[i]);
//    freopen("INPUT.txt", "r", stdin);
	while (scanf("%s%s", change, origin) != EOF) {
        memset(ori, 0, sizeof(ori));
        memset(cha, 0, sizeof(cha));
        int len = strlen(origin);
        for (int i = 0; i < len; i++)
            ori[origin[i] - 'A']++;

        len = strlen(change);
        for (int i = 0; i < len; i++)
            cha[change[i] - 'A']++;

        int (*cmparator)(const void*, const void*) = cmp;
        qsort(ori, 30, sizeof(ori[0]), cmparator);
        qsort(cha, 30, sizeof(cha[0]), cmparator);
        flag = 1;
        for (int i = 0; i < 30; i++)
            if (ori[i] != cha[i])
                flag = 0;

        if (flag)
            printf("YES\n");
        else
            printf("NO\n");
	}


	return 0;
}
