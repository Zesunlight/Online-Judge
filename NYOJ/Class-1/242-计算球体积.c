#include  <stdio.h>
#define PI 3.1415926
int main()
{
	double r;
	while(scanf("%lf", &r)!=EOF){
		printf("%d\n", (int)(r*r*r*PI*4/3+0.5));
	}
	return 0;
}
