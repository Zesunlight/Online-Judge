#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		int num[9] = {0};
		for (int i = 0; i < 9; i++) 
			scanf("%d", &num[i]);
		for (int j = 0; j < 3; j++)
			printf("%d %d %d\n", num[j], num[j+3], num[j+6]);		
		printf("\n");
	}
	//直接定义九个数，按顺序输出即可 
	return 0;
} 
