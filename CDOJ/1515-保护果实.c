#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	int sum = 0;
	int max = 0;
	int value = 0;
	int count = 0;
	while (total > 0) {
		scanf("%d", &value);
		count++;
		sum += value;
		if (max < value)
			max = value;
		if ((sum - max) > max && count >= 3) {
			printf("%d", count);
			break;
		}
		total--;	
	}
	if (total <= 0)
		printf("-1");
	return 0;
}
