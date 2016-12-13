#include <stdio.h>
#include <math.h> 
int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[total];
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d", &number[i]);
	}
	
	for( i=0; i<total; i++){
		printf("%d\n", (int)(3*pow(2,number[i])-2));
	} 
	
	return 0;
} 
 
//#include<stdio.h>
//int main()
//{
//	int n,m;
//	scanf("%d",&n);
//	while(n--)
//	{
//		scanf("%d",&m);
//		printf("%d\n",(3<<m)-2);
//	}
//	return 0;
//}        
