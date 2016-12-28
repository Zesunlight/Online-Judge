#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		double m = 0, x = 0, y = 0, z = 0;
		scanf("%lf%lf%lf%lf", &m, &x, &y, &z);
		printf("%.2lf\n", m * x * z / (y - x));
		//printf("%.2lf\n",s*a/(double)(b-a)*c);
		//看狗跑了多长时间 
	}

//	while (scanf("%d%d", &x, &n) != EOF) {
//		
//		printf("%lld\n", result);
//	}
	
	return 0;
}

