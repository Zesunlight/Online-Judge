#include <stdio.h>

char rank(int n);
int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[10];
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d", &number[i]);
	}
	
	for( i=0; i<total; i++){
		printf("%c\n", rank(number[i]));
	}

	return 0;
} 

char rank(int n)
{
	char destiny;
	switch(n/10){
		case 10:
		case 9: 
			destiny = 'A';
			break;
		case 8: 
			destiny = 'B';
			break;
		case 7:
			destiny = 'C';
			break;
		case 6:
			destiny = 'D';
			break;
		default:
			destiny = 'E';
			break;
	}
	return destiny;
}
