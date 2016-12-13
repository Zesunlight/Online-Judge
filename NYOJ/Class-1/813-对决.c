#include <stdio.h>
#include <math.h>

int main ()  								
{	
	int n = 0, k = 0;
	//n个人，k场比赛，并且恰好k场 
	scanf("%d %d", &n, &k);
	
	int i=0;
	while( n != 0){
		int a = n*n-4*k;
		float b = sqrt(a);
		int d = (int)b;
		int c = 1;
		if( b<0 || a != d*d)
			c = 0;
		int e = 1;
		if( (n+d)%2 )
			e = 0;
		
		if( c*e != 0)
			printf("YES");
		else
			printf("NO");
		i++;
		printf("\n");
		scanf("%d %d", &n, &k);
	}
	
	return 0; 
}

//#include <stdio.h>
//
//int main()
//{
//    int n,k;
//    while(scanf("%d%d",&n,&k)&&(n||k))
//    {
//        int ok=0;
//        for(int i=1;i<=n/2;i++)
//        {
//            if(i*(n-i)==k)
//                ok=1;
//				  continue;
//        }
//        if(ok)
//            printf("YES\n");
//        else
//            printf("NO\n");
//    }
//    return 0;
//}
