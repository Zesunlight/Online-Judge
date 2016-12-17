#include <stdio.h>
#include <math.h>
int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		int n = 0, k = 0;//n cigarettes,k butts can be a new cigarette 
		scanf("%d%d", &n, &k);
		int sum = n;
		int butt = n;
		for ( ; butt >= k; ) {
			sum += butt / k;
			butt = butt / k + butt - butt % k;
		}
		printf("%d\n", sum);	
	}
	
	return 0;
}

