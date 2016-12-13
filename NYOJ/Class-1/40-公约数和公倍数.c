#include <stdio.h>

int Findgcd( int a, int b);
int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[10000][4]={0};
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d %d", &number[i][0], &number[i][1]);
	}
	//number[][2]存放最大公约数 greatest common divisor
	//number[][3]存放最小公倍数 lowest common multiple
	int remainder = 1;
	int large,small;
	for( i=0; i<total; i++){
		large = number[i][0]>=number[i][1] ? number[i][0] : number[i][1];
		small = number[i][0]<number[i][1] ? number[i][0] : number[i][1];
		number[i][2] = Findgcd(large, small);
		number[i][3] = (large*small)/number[i][2];
	}
	
	for( i=0; i<total; i++){
		printf("%d %d\n", number[i][2], number[i][3]);
	}
	
	return 0;
} 

int Findgcd( int a, int b)
{	
	int remainder = a%b;
	while( remainder != 0){
		a = b;
		b = remainder;
		remainder = a%b;
	}
	return b;
} 


//#include<stdio.h>
//int main()
//{
//	unsigned int u,v,r,s,i,d;
//	scanf("%u",&s);
//	for(i=1;i<=s;i++)
//	{
//		scanf("%u%u",&u,&v);
//		d=u*v;
//		while(v!=0)
//		{
//			r=u%v;
//			u=v;
//			v=r;
//		}
//		printf("%u %u\n",u,d/u);
//	}
//	return 0;
//}
