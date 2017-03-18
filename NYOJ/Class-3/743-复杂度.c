#include <stdio.h>
int main ()  								
{	
	int n = 1, m = 1;
	static int pascal[2001][2001];
	pascal[1][1] = 1;
	for (int i = 2; i <= 2000; i++) {
		pascal[1][i] = i;
		pascal[i][i] = 1;
	}
	for (int i = 1; i <= 1999; i++)
		for (int j = 3; j <= 2000; j++)
			pascal[i][j] = (pascal[i][j-1] + pascal[i-1][j-1]) % 1009;

	while (scanf("%d %d", &m, &n) && n != 0 && m != 0) {
		printf("%d\n", pascal[m][n]);		
	}
		
	return 0;
}


 
#include <stdio.h>
#define MOD 1009
#define INF 2001
int dp[INF][INF];
void pre()
{
    int i,j;
    for(i=1;i<INF;i++)
    {
        for(j=i;j<INF;j++)
        {
            if(i==1) {dp[1][j]=j%MOD;continue;}
            if(i==j) {dp[i][j]=1;continue;}
            dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])%MOD;
        }
    }
}
int main()
{
    pre();
    int m,n;
    while(scanf("%d%d",&m,&n),m+n)
        printf("%d\n",dp[m][n]);
    return 0;
}        

