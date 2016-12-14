#include <stdio.h>
char change(int n);
int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		unsigned int n = 0;
		scanf("%d", &n);
		for ( ; n > 0; n /= 10) {
			int digit = n % 10;
			printf("%c", change(digit));
		}
		printf("\n");
	}
	
	return 0;
} 
char change(int n)
{
	char ai = '\0';
	switch (n) {
		case 0:
		case 1:
			ai = 'O';
			break;
		case 2:
		case 3:
			ai = 'T';
			break;
		case 4:
		case 5:
			ai = 'F';
			break;
		case 6:
		case 7:
			ai = 'S';
			break;
		case 8:
			ai = 'E';
			break;
		case 9:
			ai = 'N';
			break;
	}
	return ai;
}

---------------------------------
 
#include<cstdio>
char str[]="OOTTFFSSENT";
void show(int t)
{
	if(t){
		putchar(*(str+t%10));
		show(t/10);
	}
}
int main()
{
	int n,t;
        scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		show(n);
		puts("");
	}
}                
