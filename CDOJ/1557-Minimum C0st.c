#include <stdio.h>
#include <string.h>

#define max 1001
int figure[max][4];
//				a, c, l, r;
int min_cost(int figure[max][4], int n);

int main()
{
	memset(figure, 0, sizeof(figure));	
	int n = 0, s = 0;
	scanf("%d%d", &n, &s);
	
	int init = 0;
	int i = 0;
	for (; i < n; i++) {
		int j = 0;
		for (; j < 4; j++)
			scanf("%d", &figure[i][j]);
		init += figure[i][0];
	}
	
	int rest = s - init;
	int cost = 0;
	int count = 0;
	if (rest > 0) {
		while(count < n) {
			int now = min_cost(figure, n);
			int distance = figure[now][3] - figure[now][0];
			
			if(distance < rest) {
				cost += distance * figure[now][1];
				figure[now][1] = max;
				rest -= distance;
			} else {
				cost += rest * figure[now][1];
				rest = 0;
				printf("%d", cost);
				break;
			}
			
			count++;
		}
		
		if (rest > 0)
			printf("impossible");
			
	} else if (rest < 0) {
		while(count < n) {
			int now = min_cost(figure, n);
			int distance = figure[now][0] - figure[now][2];
			
			if(distance < -rest) {
				cost += distance * figure[now][1];
				figure[now][1] = max;
				rest += distance;
			} else {
				cost += -rest * figure[now][1];
				rest = 0;
				printf("%d", cost);
				break;
			}
			
			count++;
		}
		
		if (rest < 0)
			printf("impossible");
			
	} else
		printf("0");
	
	return 0;
}

int min_cost(int figure[max][4], int n)
{
	int min = figure[0][1];
	int number = 0;
	int i = 1;
	for (; i < n; i++)
		if (figure[i][1] < min) {
			min = figure[i][1];
			number = i;
		}
	return number;		
}
