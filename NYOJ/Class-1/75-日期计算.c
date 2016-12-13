#include <stdio.h>

int main()
{
	int total = 0;				//输入total组数据 
	scanf("%d", &total);
	int year, month, date;
	int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	for (int i=0; i<total; i++) {
		scanf("%d %d %d", &year, &month, &date);	//存储输入的一组数据 
		if (((year%400 == 0) || ((year%100 != 0) && (year%4 == 0))))
			days[1] = 29;
			
		int sorrow = 0;
		for (int j=0; j<month-1; j++)
			sorrow += days[j];
		
		printf("%d\n", sorrow+date);		//输出结果
		days[1] = 28;
	}
	
	return 0;
} 



//#include<stdio.h>
//int main()
//{
//	int a,b=0,c,y,m,d,fib;
//	scanf("%d",&a);
//	while(a--)
//	{
//		scanf("%d %d %d",&y,&m,&d);
//		if(y%400==0||y%100!=0&&y%4==0)
//			fib=29;
//		else fib=28;
//		for(c=1;c<=m;c++)
//		switch(c-1)
//		{
//         case 1:
//		   case 3:
//		   case 5:
//		   case 7:
//		   case 8:
//		   case 10:b+=31;break;
//		   case 2:b+=fib;break;
//		   case 4:
//		   case 6:
//		   case 9:
//		   case 11:b+=30;break;
//		}
//		b+=d;
//		printf("%d\n",b);
//		b=0;
//	}
//	return 0;
//}        

