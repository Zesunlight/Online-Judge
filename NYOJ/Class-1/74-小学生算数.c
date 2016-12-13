#include <stdio.h>

int main()
{
	int m = 1, n = 1;
	scanf("%d %d", &m, &n);
	for ( ; m&&n != 0; ) {
		int add = 0;
		int sum = m + n;
		if (((m%10) + (n%10)) >= 10)
			add++;
		if (sum / 1000 == 1)
			add++;
		if ((m/100 + n/100) < sum/100)
			add++;
		printf("%d\n", add);
		scanf("%d %d", &m, &n);
	}
	
	return 0;
} 
