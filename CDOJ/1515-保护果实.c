#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	int sum = 0;
	int max = 0;
	int value = 0;
	int count = 0;
	while (total > 0) {
		scanf("%d", &value);
		count++;
		sum += value;
		if (max < value)
			max = value;
		if ((sum - max) > max && count >= 3) {
			printf("%d", count);
			break;
		}
		total--;	
	}
	if (total <= 0)
		printf("-1");
	return 0;
}

---------------------------------------------------

#include <iostream>
#include<cstdio>
using namespace std;

int a[1000005];

int main()
{
    int n,i,m;
    int s;
    scanf("%d",&n);
    for(i = 0; i < n; i++) 
	    scanf("%d",&a[i]);
    if(n < 3) {
	    printf("-1\n"); 
	    return 0;
    }
    m = max(a[0],a[1]);
    s = min(a[0],a[1]);
    for(i = 2; i < n; i++)
    {
        if(a[i] > m)
        {
            s += m;
            m = a[i];
        }
        else s += a[i];
        if(s > m) break;
    }
    if(i < n) printf("%d\n",i + 1);
    else printf("-1\n");
    return 0;
}

