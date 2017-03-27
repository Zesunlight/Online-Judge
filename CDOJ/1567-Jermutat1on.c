#include <stdio.h>

int main()
{
	int n = 2, k = 1;
	scanf("%d%d", &n, &k);
	
	int init = k / 2 + 1;
	int flag = 1;
	if (k % 2 == 0)
		flag = 0;
	printf("%d ", init);
	
	for (int i = 1; i < k; i++) {
		if (flag == 1) {
			printf("%d ", init + i);
			init += i;
		} else {
			printf("%d ", init - i);
			init -= i;
		}
	
		flag = !flag;		
	}

	for (int j = k; j < n; j++)
		printf("%d ", j+1);
	
	return 0;
}

