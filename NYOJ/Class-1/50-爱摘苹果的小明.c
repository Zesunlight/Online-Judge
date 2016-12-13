#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	int apple[10] = {0};
	int hand = 100;
	for (int i=0; i<total; i++) {
		for (int j=0; j<10; j++)
			scanf("%d", &apple[j]);
		scanf("%d", &hand);
		hand += 30;
		
		int can = 0;
		for (int k=0; k<10; k++)
			if (hand >= apple[k])
				can++;
				
		printf("%d\n", can);
	}
	
	return 0;
}
