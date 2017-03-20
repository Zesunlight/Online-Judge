#include <stdio.h>

int main()  								
{	
	int x1 = 1, y1 = 1, x2 = 1, y2 = 1, x3 = 1, y3 = 1;
	while (scanf("%d%d%d%d%d%d", &x1, &y1, &x2, &y2, &x3, &y3) != EOF && 
			(x1 != 0 || y1 != 0 || x2 != 0 || y2 != 0 || x3 != 0 || y3 != 0)) {
				int clock = 0;
				if (x1 != x2) {
					double slope = (y2 - y1) / (double)(x2 - x1);
					double intercept = (double)y1 - x1 * slope;
					double judge = slope * x3 + intercept - y3;
					if (x2 > x1) {
						if (judge > 0)		//C在直线AB的下方
							clock = 1;
					} else {
						if (judge < 0) 		//C在直线AB的下方
							clock = 1;
					}								
				} else {			//AB垂直于y轴 
					if (y2 > y1) {
						if (x3 > x1)
							clock = 1;
					} else {
						if (x3 < x1)
							clock = 1;
					}
				}
				printf("%d\n", clock);
			}
			
	return 0;
}

 
//#include<iostream>
//using namespace std;
//int main()
//{
//	while(1)
//	{
//		int x1,y1,x2,y2,x3,y3;
//		cin>>x1>>y1>>x2>>y2>>x3>>y3;
//		if(x1==0&&y1==0&&x2==0&&y2==0&&x3==0&&y3==0)
//			break;
//		int ax=x2-x1,ay=y2-y1,bx=x2-x3,by=y2-y3;
//		if(ax*by-ay*bx<0)		//向量叉乘 
//			cout<<0<<endl;
//		else
//			cout<<1<<endl;
//	}
//		
//}
