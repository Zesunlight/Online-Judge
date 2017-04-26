#include <stdio.h>
#include <string.h>
int main()
{
	int n = 0;	
	scanf("%d", &n);
	while (n--) {
		int much = 0;
		scanf("%d", &much);
		int num[10] = {0};
		
		while (much > 0) {
			char c[6];
			sprintf(c, "%d", much);
			for (int i = 0; c[i] != '\0'; i++)
				num[c[i] - '0']++;
			much--;	
		}		
	
		for (int i = 0; i < 10; i++) {
			printf("%d", num[i]);
			if (i != 9)
				printf(" ");
		}
		printf("\n");
	}
	
	//another way
//	while(much!=0) {
//		t=much%10;
//		num[t]++;
//		much/=10;
//	}
	
	return 0;
}
