#include <stdio.h>
int time(int n);
int main()
{
    int total = 0;
    scanf("%d", &total);
    while (total--) {
        int n = 0;
        scanf("%d", &n);
        printf("%d\n", time(n));
    }
    return 0;
}
int time(int n)
{
    int result = 0;

    if (n == 1)
        result = 0;
    else if (n == 2)
        result = 1;
    else if (n % 2 == 0)
        result = time(n / 2) + 1;
    else
        result = time(n / 2) + 2;

    return result;
}

-----------------------------------------------

#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int n,m,cnt;
	cin>>n;
	while(n--)
	{
              cin>>m;
              cnt=0;
              while(m)
              {
                      if(m&1)   //m是奇数，按位与
                        cnt++;
                      cnt++;
                      m>>=1;    //右移一位，即除以2
              }
              cout<<cnt-2<<endl;
	}
}

---------------------------------------------------
/*------另外一种思路
这个表示与二进制有关系，规律举例子可以得出。
例如：n=15；那么8 < 15 < 2*8,所以指数肯定为8加上15-8，
才会使得乘的次数最少。对于指数为8所需要的次数，
因为8由每次乘2所得，所以相当于左移一位，
移动的次数就是得到8乘的次数。由于8得到了，
此过程中又得到了4,2,1, 15-8肯定由这几个数得到，每个数对应15的二进制的一个一，
所以用8的次数加上15-8对应数的1的位数，就是结果，
总的来说，就是得到15的最高位需要的次数，再加上出去最高位后1的位数就是结果。
*/
