#include <stdio.h>
int main()
{
	int number[1000]={0};
	int i = 1;
	
	scanf("%d", &number[0]);
	for( ; number[i-1] != 0; i++){
		scanf("%d", &number[i]);
	}
	
	int a,b,c;
	for( i=0; number[i] != 0; i++){
		a = number[i]/100;
		c = number[i]%10;
		b = (number[i]-100*a-c)/10;
		
		if( a*a*a+b*b*b+c*c*c == number[i]){
			printf("Yes\n");
		} else {
			printf("No\n");
		}
	}
	
	return 0;
}
