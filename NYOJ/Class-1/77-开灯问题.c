#include <stdio.h>

void change(int* lights, int a);
int main()
{
	int n = 0, k = 0;
	//nÕµµÆ£¬k¸öÈË
	
	scanf("%d %d", &n, &k);
	int lights[n+1];
	for (int i=0; i<=n; i++) {
		lights[i] = 1;
	}
	
	for (int i=2; i<=k; i++) {
		for (int j=i; j<=n; ) {
			change(lights, j);
			j = j + i;
		}
	} 
	
	for (int i=1; i<=n; i++)
		if (lights[i] == 1)
			printf("%d ", i);
	
	return 0;
}

void change(int* lights, int a)
{
	if (lights[a] == 1)
		lights[a] = 0;
	else
		lights[a] = 1;
}
