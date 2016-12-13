#include <stdio.h>
int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[1000]={0};
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d", &number[i]);
	}
	
	int sum = 0;
	for( i=0; i<total; i++){
		for( sum=0; number[i]>0; ){
			sum += number[i]%2;
			number[i]/=2;
		}
		printf("%d\n", sum);
	}
	
	return 0;
} 
