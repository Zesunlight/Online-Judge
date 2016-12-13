#include <stdio.h>

int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[total][2];
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d", &number[i][0]);
	}
	
	int rate = 1;
	int puppet = 10;
	for( i=0; i<total; i++){
		rate = 1;
		puppet = number[i][0];
		do{	
			puppet /= 10;
			rate *= 10;
		}while(puppet >= 10);
		number[i][1] = number[i][0]%rate;
	}
	
	for( i=0; i<total; i++){
		printf("%d\n", number[i][1]);
	}
	
	return 0;
} 
