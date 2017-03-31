#include <stdio.h>
#include <string.h>
#include <math.h>

int figure[101][101];

int main()
{
	memset(figure, 0, sizeof(figure));	
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	
	int n = 0, value = 1;
	scanf("%d", &n);
	int x = 0, y = n - 1;
	figure[x][y] = 1;
	
	while (value < n*n) {
		while (x+1 < n && figure[x+1][y] == 0)
			figure[++x][y] = ++value;
		while (y-1 >= 0 && figure[x][y-1] == 0)
			figure[x][--y] = ++value;
		while (x-1 >= 0 && figure[x-1][y] == 0)
			figure[--x][y] = ++value;
		while (y+1 < n && figure[x][y+1] == 0)
			figure[x][++y] = ++value;
	}
	
	for (x = 0; x < n; x++) {
		for (y = 0; y < n; y++)
			printf("%d ", figure[x][y]);
		printf("\n");
	}
		
//	printf("%lld", sum);
	
	return 0;
}


 
#include<stdio.h>
int main()
{
	int a,b,c,d,n,sum=1;
	int yi[101][101];
	scanf("%d",&n);
	for(a=0;a<=(n-1)/2;a++)
	{
		for(b=a;b<=n-a-1;b++)
			yi[b][n-a-1]=sum++;
		for(b=n-2-a;b>=a;b--)
			yi[n-a-1][b]=sum++;
		for(b=n-a-2;b>=a;b--)
			yi[b][a]=sum++;
		for(b=a+1;b<n-a-1;b++)
			yi[a][b]=sum++;
	}
	for(c=0;c<n;c++)
	{
		for(d=0;d<n;d++)
			printf("%d ",yi[c][d]);
		printf("\n");
	}
}        
