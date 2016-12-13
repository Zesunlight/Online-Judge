#include <stdio.h>
void crack(int c);

int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[total];
	int i = 0;
	for ( i=0; i<total; i++) {
		scanf("%d", &number[i]);
	}
	
	for ( i=0; i<total; i++) {
		crack(number[i]);
	}
	
	return 0;
} 

void crack(int c)
{
	int a = 1, b = c+1;
	do {
		if ((b*c) % (b-c) == 0) {
			a = (b*c) / (b-c);
			printf("1/%d=1/%d+1/%d\n", c, a, b);
		}
		b++;
	} while (a != b-1);
} 

//#include<stdio.h>
//int main()
//{
//	int s,n,i;
//	scanf("%d",&s);
//	while(s--){
//		scanf("%d",&n);
//		for(i=n+1;i<=2*n;++i)	//注意较小的数的上下限 
//			if(n*i%(i-n)==0)
//				printf("1/%d=1/%d+1/%d\n",n,n*i/(i-n),i);
//	}
//}        

