#include <stdio.h>
#include <math.h>
int main()
{
//	int total = 0;
//	scanf("%d", &total);
	int count = 0;
	int n[4] = {0};
	while (~scanf("%d%d%d%d",&n[0],&n[1],&n[2],&n[3])) {
		int max2 = 0, max = 0;
		++count;		
		for (int i = 0; i < 4; i++) {
			if (n[i] > max)
				max = n[i];
		}
		int flag = 1;
		for (int i = 0; i < 4; i++) {
			if (flag)
				if (n[i] == max) {
					n[i] = 0;
					flag = 0;
				}
				
			if (n[i] > max2)
				max2 = n[i];
		}
		printf("Case %d: %d\n", count, max + max2);
	}
	
	return 0;
}

