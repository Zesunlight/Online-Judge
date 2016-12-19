#include <stdio.h>
#include <string.h>
int main()
{
    int total = 0;
    scanf("%d", &total);
    while (total--) {
        char str[1000001];
        scanf("%s", str);
        int sum = 0;
        int len = strlen(str);
        for (int i = 0; i < len; i++) {
            sum += str[i] - '0';
            sum = sum % 9;
        }
        printf("%d\n", sum);
    }
    return 0;
}

--------------------------------------------------
//为什么不行呢？？？ 
#include <stdio.h>
int main()
{
    int total = 0;
    scanf("%d", &total);
    int c = 32;
    c = getchar();  //接收输入整数m后换行符
    while (total--) {
        c = getchar();  //接收数n的首位数字
        int sum = 0;
        while (c != '\n') { //若c是换行符，表示一个数字已经输完
            sum += c - '0';
            sum = sum % 9;
            c = getchar();  //输完数n后的下一位数字或者是换行符
            while ((c != '\n') && (c < '0' || c > '9'))
                c = getchar();
        }
        printf("%d\n", sum);
    }
    return 0;
}

------------------------------------------------
 
#include<cstdio>
using namespace std;
int mod9(char *str)
{
	int sum=0;
	char *p=str;
	while(*p)
	{
		sum+=*p-'0';
		++p;
	}
	return sum%9;
}
char m[1000010];
int main()
{
	int n;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%s",&m);
		printf("%d\n",mod9(m));
	}
}

