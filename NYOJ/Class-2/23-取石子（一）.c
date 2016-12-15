#include <stdio.h>

int main()
{
	int n = 0, m = 0;
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		scanf("%d%d", &n, &m);
		//n is the number of stone, m is the max can take
		int rest = n % (m + 1);
		if (rest != 0)
			printf("Win\n");
		else
			printf("Lose\n");		
		
	}
	
	return 0;
} 
