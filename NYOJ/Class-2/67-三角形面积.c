#include <stdio.h>
double absf(double n);
int main()
{
	double x1, x2, x3, y1, y2, y3;
	scanf("%lf%lf%lf%lf%lf%lf", &x1, &y1, &x2, &y2, &x3, &y3);
	while (x1 != 0.0 || x2 != 0.0 || x3 != 0.0 ||
			y1 != 0.0 || y2 != 0.0 || y3 != 0.0) {
				double one = (y1 + y2) * (x2 - x1);
				double two = (y2 + y3) * (x3 - x2);
				double three = (y3 + y1) * (x3 - x1);
			//s=(x1*y2+y1*x3+x2*y3)-(x1*y3+y2*x3+y1*x2);
			
				printf("%.1lf\n", absf(three - one - two)/2);
				scanf("%lf%lf%lf%lf%lf%lf", &x1, &y1, &x2, &y2, &x3, &y3);				
			}
	return 0;
} 
double absf(double n)
{
	if (n >= 0.0)
		return n;
	else
		return -n;
}
