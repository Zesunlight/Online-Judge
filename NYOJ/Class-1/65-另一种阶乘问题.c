#include <stdio.h>

int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[total];
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d", &number[i]);
	}
	
	int factorial[20]={1};
	factorial[1]=1;
	for( i=2; i<20;){
		factorial[i]=(i+1)*factorial[i-2];
		factorial[i+1] = factorial[i];
		i += 2;
	}
	factorial[19]=factorial[18];
	
//	for( i=0; i<20; i++){
//		printf("%d\n", factorial[i]);
//	}
	int sum=0;
	for( i=0; i<total; i++){
		sum = 0; 
		for(int j=number[i]-1; j>=0; j--){
			sum += factorial[j];
		}
		printf("%d\n", sum);
	}
	
	return 0;
} 
